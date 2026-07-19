import sqlite3

conexao = sqlite3.connect("database/biblioteca.db")
cursor = conexao.cursor()

livros = [
    ("Dom Casmurro", "Machado de Assis"),
    ("Meu Pé de Laranja Lima", "José Mauro Vasconcelos"),
    ("Harry Potter e a Pedra Filosofal", "J. K. Rowling"),
    ("O Hobbit", "J. R. R. Tolkien"),
    ("Percy Jackson", "Rick Riordan"),
    ("Rádio Silêncio", "Alice Oseman"),
    ("Capitães da Areia", "Jorge Amado"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
]

cursor.executemany(
    """
    INSERT INTO livros (titulo, autor)
    VALUES (?, ?)
    """,
    livros
)

conexao.commit()
conexao.close()

print("Livros cadastrados com sucesso!")