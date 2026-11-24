# Proposta: Criação do Sistema Agenda do Salão

## Contexto
Um salão de cabeleireiro precisa substituir o controle manual em papel por um sistema web simples para cadastrar clientes e organizar horários marcados.

## Escopo da Mudança
- Criar banco de dados SQLite com duas tabelas relacionadas (`clientes` e `agendamentos`).
- Implementar CRUD completo para ambas as entidades em Flask.
- Garantir validações de negócio (bloqueio de horários duplicados e proteção contra exclusão de clientes com agendamentos).
