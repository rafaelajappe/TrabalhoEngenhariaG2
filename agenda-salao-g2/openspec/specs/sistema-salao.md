# Especificação Final: Sistema Agenda do Salão

## 1. Modelo de Dados (SQLite)

### Tabela `clientes`
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `nome`: TEXT NOT NULL
- `telefone`: TEXT NOT NULL

### Tabela `agendamentos`
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `cliente_id`: INTEGER NOT NULL (Chave Estrangeira referenciando `clientes(id)`)
- `servico`: TEXT NOT NULL
- `data_hora`: TEXT NOT NULL

## 2. Requisitos Funcionais (CRUD Completo)

### Clientes
- **Criar (`POST /clientes/novo`):** Cadastra novo cliente com `nome` e `telefone`.
- **Listar (`GET /clientes`):** Exibe todos os clientes cadastrados em ordem alfabética.
- **Alterar (`POST /clientes/editar/<id>`):** Atualiza `nome` e `telefone` de um cliente existente.
- **Excluir (`POST /clientes/excluir/<id>`):** Remove um cliente, desde que não possua agendamentos vinculados.

### Agendamentos
- **Criar (`POST /agendamentos/novo`):** Registra novo agendamento vinculando `cliente_id`, `servico` e `data_hora`.
- **Listar (`GET /agendamentos`):** Lista todos os agendamentos ordenados por data/hora, exibindo o nome do cliente.
- **Alterar (`POST /agendamentos/editar/<id>`):** Permite alterar cliente, serviço ou data/hora de um agendamento existente.
- **Excluir (`POST /agendamentos/excluir/<id>`):** Cancela/remove um agendamento.

## 3. Regras de Negócio Obrigatórias
- **RN01 (Conflito de Horário):** O sistema deve impedir o cadastro ou alteração de um agendamento caso já exista outro registro com a exata mesma `data_hora`.
- **RN02 (Integridade de Cliente):** O sistema deve bloquear a exclusão de um cliente caso exista ao menos um agendamento vinculado ao seu `id`.
