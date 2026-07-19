# Sistema de Aluguel de Livros MOM

## Descrição

Este projeto demonstra a utilização de Middleware Orientado a Mensagens (MOM) utilizando o paradigma de Filas de Mensagens (Message Queue). O sistema simula o aluguel de livros de uma biblioteca.

Quando um usuário solicita o aluguel de um livro, o Producer envia uma mensagem para uma fila do RabbitMQ.

Dois consumidores ficam aguardando mensagens e apenas um deles processa cada pedido.

## 🔧 Setup e Instalação

### 1. Instalar dependências

```
pip install -r requirements.txt
```

### 2. Subir RabbitMQ

```
docker compose up -d
```

### 3. Criar banco

```
python database/criar_banco.py
```

### 4. Popular banco

```
python database/popular_banco.py
```

### 5. Executar consumidor 1

```
python -m consumers.consumer1
```

### 6. Executar consumidor 2

```
python -m consumers.consumer2
```

### 7. Executar producer

```
python -m producer.producer
```

## Saída Esperada

1. Inicie os dois consumidores.
2. Execute o Producer.
3. Envie pedidos de aluguel.
4. Observe que apenas um consumidor processa cada mensagem.
5. Feche um consumidor.
6. Envie novas mensagens.
7. Observe que o outro consumidor continua processando normalmente.