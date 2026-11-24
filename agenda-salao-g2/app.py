import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave-secreta-salao-g2"
DB_NAME = "salao.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                servico TEXT NOT NULL,
                data_hora TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        """)


@app.route("/")
def index():
    return redirect(url_for("listar_agendamentos"))


# --- CRUD CLIENTES ---
@app.route("/clientes")
def listar_clientes():
    with get_db() as conn:
        clientes = conn.execute("SELECT * FROM clientes ORDER BY nome").fetchall()
    return render_template("clientes.html", clientes=clientes)


@app.route("/clientes/novo", methods=["POST"])
def criar_cliente():
    nome = request.form["nome"].strip()
    telefone = request.form["telefone"].strip()
    if nome and telefone:
        with get_db() as conn:
            conn.execute("INSERT INTO clientes (nome, telefone) VALUES (?, ?)", (nome, telefone))
        flash("Cliente cadastrado com sucesso!", "sucesso")
    return redirect(url_for("listar_clientes"))


@app.route("/clientes/editar/<int:id>", methods=["POST"])
def editar_cliente(id):
    nome = request.form["nome"].strip()
    telefone = request.form["telefone"].strip()
    with get_db() as conn:
        conn.execute("UPDATE clientes SET nome = ?, telefone = ? WHERE id = ?", (nome, telefone, id))
    flash("Cliente atualizado com sucesso!", "sucesso")
    return redirect(url_for("listar_clientes"))


@app.route("/clientes/excluir/<int:id>", methods=["POST"])
def excluir_cliente(id):
    with get_db() as conn:
        vinculados = conn.execute(
            "SELECT COUNT(*) as total FROM agendamentos WHERE cliente_id = ?", (id,)
        ).fetchone()["total"]
        if vinculados > 0:
            flash("Erro: Não é possível excluir cliente que possui agendamento vinculado!", "erro")
        else:
            conn.execute("DELETE FROM clientes WHERE id = ?", (id,))
            flash("Cliente excluído com sucesso!", "sucesso")
    return redirect(url_for("listar_clientes"))


# --- CRUD AGENDAMENTOS ---
@app.route("/agendamentos")
def listar_agendamentos():
    with get_db() as conn:
        agendamentos = conn.execute("""
            SELECT a.id, a.cliente_id, a.servico, a.data_hora, c.nome AS cliente_nome
            FROM agendamentos a
            JOIN clientes c ON a.cliente_id = c.id
            ORDER BY a.data_hora
        """).fetchall()
        clientes = conn.execute("SELECT * FROM clientes ORDER BY nome").fetchall()
    return render_template("agendamentos.html", agendamentos=agendamentos, clientes=clientes)


@app.route("/agendamentos/novo", methods=["POST"])
def criar_agendamento():
    cliente_id = request.form["cliente_id"]
    servico = request.form["servico"].strip()
    data_hora = request.form["data_hora"]
    with get_db() as conn:
        conflito = conn.execute(
            "SELECT id FROM agendamentos WHERE data_hora = ?", (data_hora,)
        ).fetchone()
        if conflito:
            flash("Erro: Já existe um agendamento marcado para este mesmo horário!", "erro")
        else:
            conn.execute(
                "INSERT INTO agendamentos (cliente_id, servico, data_hora) VALUES (?, ?, ?)",
                (cliente_id, servico, data_hora),
            )
            flash("Agendamento realizado com sucesso!", "sucesso")
    return redirect(url_for("listar_agendamentos"))


@app.route("/agendamentos/editar/<int:id>", methods=["POST"])
def editar_agendamento(id):
    cliente_id = request.form["cliente_id"]
    servico = request.form["servico"].strip()
    data_hora = request.form["data_hora"]
    with get_db() as conn:
        conflito = conn.execute(
            "SELECT id FROM agendamentos WHERE data_hora = ? AND id != ?", (data_hora, id)
        ).fetchone()
        if conflito:
            flash("Erro: Horário já ocupado por outro agendamento!", "erro")
        else:
            conn.execute(
                "UPDATE agendamentos SET cliente_id = ?, servico = ?, data_hora = ? WHERE id = ?",
                (cliente_id, servico, data_hora, id),
            )
            flash("Agendamento atualizado com sucesso!", "sucesso")
    return redirect(url_for("listar_agendamentos"))


@app.route("/agendamentos/excluir/<int:id>", methods=["POST"])
def excluir_agendamento(id):
    with get_db() as conn:
        conn.execute("DELETE FROM agendamentos WHERE id = ?", (id,))
    flash("Agendamento excluído com sucesso!", "sucesso")
    return redirect(url_for("listar_agendamentos"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
