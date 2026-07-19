import sqlite3

CAMINHO_BANCO = "database/biblioteca.db"


def conectar():
    return sqlite3.connect(CAMINHO_BANCO)


def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id, titulo, autor, disponivel
    FROM livros
    ORDER BY id
    """)

    livros = cursor.fetchall()

    conexao.close()

    return livros


def livro_disponivel(id_livro):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT disponivel
    FROM livros
    WHERE id = ?
    """, (id_livro,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return False

    return resultado[0] == 1


def alugar_livro(id_livro):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 0
    WHERE id = ?
    """, (id_livro,))

    conexao.commit()

    conexao.close()


def buscar_livro(id_livro):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT titulo, autor
    FROM livros
    WHERE id = ?
    """, (id_livro,))

    livro = cursor.fetchone()

    conexao.close()

    return livro