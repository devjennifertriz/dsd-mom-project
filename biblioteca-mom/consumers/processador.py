import time
from logs.logger import registrar

from database.repo import (
    buscar_livro,
    livro_disponivel,
    alugar_livro
)


def processar_aluguel(id_livro, consumidor):

    print("=" * 50)
    registrar(f"{consumidor} recebeu o livro {id_livro}")
    print(f"\n[{consumidor}] Recebido pedido do livro {id_livro}")

    livro = buscar_livro(id_livro)
    if livro is None:

        registrar("Livro inexistente.")

        print("Livro inexistente.")

        return

    titulo, autor = livro

    registrar(f"Livro encontrado: {titulo}")
    if not livro_disponivel(id_livro):
        registrar(f"{titulo} já estava alugado.")
        print("Livro indisponível.")
        return

    print("Status: Processando...")
    time.sleep(3)
    alugar_livro(id_livro)
    print("=" * 50)
    registrar(f"{titulo} alugado com sucesso.")
    print("✔ Aluguel concluído.")