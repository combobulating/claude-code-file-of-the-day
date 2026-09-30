#!/bin/bash
# Stop hook: a short sound at the end of a Claude reply tells whose move is next.
# A voice is heard by the neighbours and gets annoying, while a tone carries exactly one meaning.
#
# The signal does not fire on a timer. It sounds only if Claude, before its last
# message, put a word into the signal file /tmp/claude_signal_<session_id>:
#   done - the work is closed, nothing is needed from you (a ringing tone);
#   need - you are needed next: a decision, access, a manual action, a look (a lower tone).
# No file or an empty file - the hook stays silent.
# An unknown word counts as need: you will survive an extra call,
# while a missed one leaves you waiting at a silent window.
# Never blocks (exit 0): the sound is its only action.

INPUT=$(cat)
SID=$(echo "$INPUT" | jq -r '.session_id // "default"' 2>/dev/null)
[ -z "$SID" ] && SID="default"

SOUND_DIR="$HOME/.claude/sounds"

# Quiet hours: from QUIET_FROM to QUIET_TO by the computer clock there is no sound.
QUIET_FROM=20
QUIET_TO=9

# 10# - decimal parsing, otherwise 08 and 09 are read as invalid octal.
h=$((10#$(date +%H)))
# Quiet hours across midnight (from 22 to 8) and within the day (from 1 to 6) are counted differently.
if [ "$QUIET_FROM" -gt "$QUIET_TO" ]; then
    { [ "$h" -ge "$QUIET_FROM" ] || [ "$h" -lt "$QUIET_TO" ]; } && exit 0
else
    { [ "$h" -ge "$QUIET_FROM" ] && [ "$h" -lt "$QUIET_TO" ]; } && exit 0
fi

# The signal file with the word. No word - we stay silent.
SIGNAL_FILE="/tmp/claude_signal_${SID}"
[ -f "$SIGNAL_FILE" ] || exit 0

# The word: the first word of the first non-empty line, at most 32 bytes, lowercase.
# The carriage return is removed, otherwise a word from a Windows file will not match.
# An empty file is not a signal: delete it and stay silent.
MARK=$(head -c 32 "$SIGNAL_FILE" | tr -d '\000\r' | tr -s ' \t\n' '\n' | grep -m 1 . | tr '[:upper:]' '[:lower:]')
if [ -z "$MARK" ]; then
    rm -f "$SIGNAL_FILE"
    exit 0
fi

case "$MARK" in
    done) FILE="$SOUND_DIR/done.wav" ;;
    *)    FILE="$SOUND_DIR/need.wav" ;;
esac

# No sound file - the word is not deleted: the signal plays as soon as the sounds are back in place.
[ -f "$FILE" ] || exit 0
rm -f "$SIGNAL_FILE"

nohup afplay "$FILE" >/dev/null 2>&1 &
exit 0
