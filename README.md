# PDV com Descontos Progressivos

Sistema de Ponto de Venda (PDV) em Python que aplica descontos progressivos
por idade e por valor da compra, com histórico em memória e resumo final do dia.


---

## Sobre o projeto

Este projeto simula a lógica de um PDV (Ponto de Venda) de loja, farmácia ou
supermercado. O programa recebe o valor da compra e a idade do cliente, aplica
descontos progressivos conforme regras de negócio e exibe o valor final. Ao
encerrar, mostra um resumo consolidado do dia com quantidade de compras,
total bruto, total de descontos e total a pagar.

O objetivo é praticar lógica de programação com estruturas de repetição,
condicionais, validação de entrada, acumuladores e formatação de saída.

---

## Funcionalidades

- Registro de compras com valor e idade do cliente
- Desconto de 20% para clientes com 65 anos ou mais
- Desconto extra de 10% para compras acima de R$ 100 (após o desconto de idade)
- Loop de compras até o usuário digitar `0`
- Validação de valores negativos e idades inválidas
- Histórico de compras em memória
- Resumo final com quantidade, total bruto, descontos e total a pagar

---

## Pré-requisitos

- Python 3.8 ou superior
- Git => opcional, apenas para clonar o repositório

---

## Como rodar

 Clone o repositório:
    ```bash 
    git clone https://github.com/Crisbr4l/nivel_1.git
    cd nivel_1
    python pvd.py 
    ``` 



