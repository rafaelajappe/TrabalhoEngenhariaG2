# Projeto: Agenda do Salão

## Visão Geral
Sistema web desenvolvido em Python com Flask e banco de dados SQLite para gerenciar o cadastro de clientes e o agendamento de serviços de um salão de cabeleireiro.

## Stack Tecnológica
- **Linguagem:** Python 3
- **Framework Web:** Flask
- **Banco de Dados:** SQLite (`salao.db`)
- **Frontend:** HTML5 + CSS3 (Templates Jinja2)

## Arquitetura e Decisões
- Aplicação monolítica enxuta concentrada em `app.py` para facilitar execução e manutenção.
- Criação automática das tabelas na inicialização do sistema (`init_db()`).
- Uso de `PRAGMA foreign_keys = ON` no SQLite para garantir integridade referencial.
