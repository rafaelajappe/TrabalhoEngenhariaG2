# Delta Spec: 2026-11-19-criar-sistema

## Adicionado
- Tabela `clientes` (`id`, `nome`, `telefone`).
- Tabela `agendamentos` (`id`, `cliente_id`, `servico`, `data_hora`).
- Endpoints Flask para Criar, Listar, Alterar e Excluir clientes e agendamentos.
- Validação de unicidade de `data_hora` nos agendamentos.
- Validação de contagem de agendamentos antes da exclusão de clientes.
