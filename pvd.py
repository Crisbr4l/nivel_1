shopping = []

gross_total = 0.0
discount_total = 0.0
final_total = 0.0

while True:
    value = float(input("Qual o valor: (0 = encerrar):"))
    if value == 0:
        break
    if value < 0:
        print("valor invalido!")
        continue
    age = int(input("Idade: "))
    while age < 0:
        print("Idade invalida")
        idade = int(input("Digite aa idade novamente: "))
    final_value = value
    if age >= 65:
        final_value *= 0.80
    if final_value > 100:
        final_value *= 0.90
    discount = value - final_value
    print(f" O valor fianl é R${final_value:,.2f} ")

    shopping.append({"gross": value, "final": final_value, "discount": discount})

    gross_total += value
    discount_total += discount
    final_total += final_value

    print(
        f"Resumo quantidade {len(shopping)} Total {gross_total} {discount_total} {final_total}"
    )
