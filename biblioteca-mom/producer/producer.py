import json
import pika

import database.repo
from database.repo import listar_livros
from producer.rabbitmq import conectar, FILA

connection, channel = conectar()


def mostrar_livros():

    print("\n==== LIVROS DA BIBLIOTECA ====\n")

    for livro in database.repo.listar_livros():

        status = "Disponível" if livro[3] == 1 else "Alugado"

        print(
            f"{livro[0]} - {livro[1]} ({livro[2]}) - {status}"
        )


while True:

    mostrar_livros()

    print("\n0 - Sair")

    escolha = input("\nDigite o ID do livro: ")

    if escolha == "0":
        break

    mensagem = {
        "livro_id": int(escolha)
    }

    channel.basic_publish(
        exchange="",
        routing_key=FILA,
        body=json.dumps(mensagem),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print("\nSolicitação enviada para a fila!\n")


connection.close()