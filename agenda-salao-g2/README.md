# Agenda do Salão

Trabalho G2 de Engenharia de Software. Sistema simples para um salão de cabeleireiro cadastrar clientes e marcar horários.

**Integrantes:** Rafaela Jappe, Jessika Catharina e Augusto Pasetto

## Banco de dados (SQLite)
- `clientes`: `id`, `nome`, `telefone`
- `agendamentos`: `id`, `cliente_id` (liga com `clientes`), `servico`, `data_hora`

Um cliente pode ter vários agendamentos.

## CRUD

| Entidade | Criar | Listar | Alterar | Excluir |
| :--- | :---: | :---: | :---: | :---: |
| **Clientes** | sim | sim | sim | sim |
| **Agendamentos** | sim | sim | sim | sim |

**Regras de Negócio:**
- Não pode marcar dois horários iguais (`data_hora` única).
- Não pode excluir cliente que tem agendamento vinculado.

## Como rodar
```bash
pip install flask
python app.py
```
Depois abra `http://127.0.0.1:5000` no navegador.

## Como usamos o OpenSpec
1. **Explore:** conversamos com a IA sobre a ideia e as regras, sem escrever código.
2. **Propose:** a IA escreveu a proposta, as tarefas e as specs em Markdown.
3. **Apply:** a IA gerou o `app.py` e os templates seguindo as specs.
4. **Archive:** arquivamos a mudança e as specs finais ficaram em `openspec/specs/`.

## Arquivos do Projeto
```text
app.py                                              # todo o sistema (banco + CRUD)
templates/                                          # páginas HTML
openspec/project.md                                 # sobre o projeto
openspec/specs/                                     # specs finais
openspec/changes/archive/2026-11-19-criar-sistema/  # proposta, tarefas e specs
```
