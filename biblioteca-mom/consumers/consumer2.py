import json
import pika

from consumers.processador import processar_aluguel

FILA = "aluguel_livros"

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


def callback(ch, method, properties, body):

    mensagem = json.loads(body)

    processar_aluguel(
        mensagem["livro_id"],
        "Consumidor 2"
    )

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )


channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue=FILA,
    on_message_callback=callback
)

print("Consumidor 2 aguardando mensagens...")

channel.start_consuming()