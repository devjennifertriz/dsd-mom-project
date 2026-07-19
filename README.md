# Sistema de Aluguel de Livros utilizando RabbitMQ

## Descrição

Este projeto demonstra a utilização de Middleware Orientado a Mensagens (MOM)
utilizando o paradigma de Filas de Mensagens (Message Queue).

O sistema simula o aluguel de livros de uma biblioteca.

Quando um usuário solicita o aluguel de um livro, o Producer envia uma
mensagem para uma fila do RabbitMQ.

Dois consumidores ficam aguardando mensagens e apenas um deles processa cada
pedido.

## Tecnologias

- Python 3
- RabbitMQ
- Docker
- SQLite
- Pika

## Estrutura

```
biblioteca-mom/
database/
producer/
consumers/
logs/
requirements.txt
docker-compose.yml
```

## Fluxo

```
Producer

↓

RabbitMQ

↓

Fila aluguel_livros

↓

Consumidor 1

OU

Consumidor 2

↓

Banco SQLite
```

## Como executar

### Instalar dependências

```
pip install -r requirements.txt
```

### Subir RabbitMQ

```
docker compose up -d
```

### Criar banco

```
python database/criar_banco.py
```

### Popular banco

```
python database/popular_banco.py
```

### Executar consumidor 1

```
python -m consumers.consumer1
```

### Executar consumidor 2

```
python -m consumers.consumer2
```

### Executar producer

```
python -m producer.producer
```

## Demonstração

1. Inicie os dois consumidores.
2. Execute o Producer.
3. Envie pedidos de aluguel.
4. Observe que apenas um consumidor processa cada mensagem.
5. Feche um consumidor.
6. Envie novas mensagens.
7. Observe que o outro consumidor continua processando normalmente.