import sqlite3

conexao = sqlite3.connect("database/biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
SELECT id, titulo, autor, disponivel
FROM livros
ORDER BY id
""")

livros = cursor.fetchall()

print("\n===== LIVROS =====\n")

for livro in livros:

    status = "Disponível" if livro[3] == 1 else "Alugado"

    print(f"""
ID: {livro[0]}
Título: {livro[1]}
Autor: {livro[2]}
Status: {status}
""")

conexao.close()