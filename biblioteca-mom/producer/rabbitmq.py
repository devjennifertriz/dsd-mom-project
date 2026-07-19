import pika

FILA = "aluguel_livros"


def conectar():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="localhost",
            credentials=pika.PlainCredentials(
                "admin",
                "admin"
            )
        )
    )

    channel = connection.channel()

    channel.queue_declare(
        queue=FILA,
        durable=True
    )

    return connection, channel