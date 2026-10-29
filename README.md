# PDV com Descontos

Um programa simples em Python que simula um caixa de loja. Você digita o valor da compra e a idade do cliente, e ele calcula o desconto e mostra quanto ficou. No final, mostra um resumo de tudo que foi vendido.

---

## O que ele faz

- Pede o valor da compra e a idade do cliente
- Dá 20% de desconto pra quem tem 65 anos ou mais
- Se depois desse desconto ainda ficar acima de R$ 100, dá mais 10% em cima
- Fica repetindo até você digitar 0
- No final mostra: quantas compras foram feitas, total sem desconto, total de desconto e total a pagar

---

## Como rodar

Precisa ter Python instalado (versão 3.8 ou mais nova).

```bash
git clone https://github.com/Crisbr4l/nivel_1.git
cd nivel_1
python pdv.py
```

---

## Exemplo de uso 
<img width="935" height="541" alt="image" src="https://github.com/user-attachments/assets/cb33c1b5-d86c-482c-80e1-15a7b7625fa4" />

```
➜  nivel_1 git:(main) ✗ python pdv.py               
Qual o valor: (0 = encerrar): 200
Idade: 65
O valor final é R$144.00 
Qual o valor: (0 = encerrar): 101
Idade: 30
O valor final é R$90.90 
Qual o valor: (0 = encerrar): 0

==============================
       RESUMO DO PEDIDO       
==============================
Quantidade de itens:         2
Total Bruto:        R$  301.00
Total de Descontos: R$   66.10
------------------------------
TOTAL A PAGAR:      R$  234.90
==============================
```

---

## Regras 
- Idade 65 ou mais → 20% de desconto
- Se o valor já com esse desconto passar de R$ 100 → mais 10% em cima
- O segundo desconto é em cima do valor já descontado, não do valor original
- Digitar 0 no valor encerra o programa
- Valor negativo ou idade negativa/texto → avisa e pede de novo

---

## O que aprendi com esse projeto 
- Fazer loop dentro de loop (um pra repetir as compras, outro pra validar a idade)
- Validar entrada com `isnumeric()`
- Somar totais com acumuladores
- Formatar número com `:.2f` e alinhar com `:>9`
- Usar branch no Git pra cada parte do projeto
- Guarda cada compra numa lista pra montar o resumo no final usando `.append()`
---



