# Registro da tarefa: uma conversa nova continua de onde paramos

Chegou uma tarefa ou um relato de erro - crie um arquivo de registro na hora, antes de qualquer outro trabalho.

Arquivo: `~/.claude/tasks/.claude-task-[short-name].md`. Se a pasta não existir, crie a pasta.

Conteúdo do arquivo: a tarefa, o que já foi feito, fatos verificados com a sua fonte, o que falta fazer.
Escreva para uma conversa nova que não sabe nada do passado.
Um resultado que existe só na resposta (uma lista, um texto, um plano) vai inteiro para o arquivo: uma conversa nova não vê as respostas anteriores.
Atualizar é reescrever: jogue fora o que o trabalho não precisa mais (relato do que foi feito, repetições, tentativas de rascunho, saídas longas de comandos) em vez de acrescentar por cima.

Ordem:
1. Chegou uma tarefa ou um erro - primeiro procure registros anteriores (passo 2).
2. Encontre todos os registros `.claude-task-*.md` dos últimos 7 dias. Existe um registro desta mesma tarefa - continue esse registro em vez de começar um novo. Existem registros sobre um tema próximo - leve os pontos principais deles para a seção “Experiência anterior”.
3. Crie o arquivo de registro.
4. A primeira linha da resposta é o caminho do arquivo.
5. A segunda linha da resposta é o que foi encontrado nos registros anteriores.
6. Atualize o arquivo antes de cada resposta.
7. Antes de a conversa ser compactada, grave no arquivo o estado completo.

As linhas dos passos 4 e 5 vão só nas respostas no chat: arquivos, código, mensagens de commit e saídas que um programa lê (JSON, CSV) não recebem nenhuma delas, nem quando essa saída é a resposta.

Comando de busca:
```bash
find ~/.claude/tasks/ -maxdepth 1 -name ".claude-task-*.md" -mtime -7 | xargs ls -lt 2>/dev/null | head -20
```

Como ficam as primeiras linhas da resposta:
> 📋 Registro da tarefa: `path/to/file.md` (atualizado)
> 🔍 Experiência anterior: [o que foi encontrado]
