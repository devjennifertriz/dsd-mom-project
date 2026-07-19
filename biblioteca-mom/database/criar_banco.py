import sqlite3

conexao = sqlite3.connect("database/biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    disponivel INTEGER NOT NULL DEFAULT 1
)
""")

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")