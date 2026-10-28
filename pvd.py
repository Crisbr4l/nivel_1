shopping = []

gross_total = 0.0
discount_total = 0.0
final_total = 0.0

while True:
    value = float(input("Qual o valor: (0 = encerrar): "))
    if value == 0:
        break
    if value < 0:
        print("valor invalido!")
        continue

    while True:
        age_input = input("Idade: ")

        if age_input.isnumeric():
            age = int(age_input)
            break
        else:
            print("Idade inválida! Digite apenas números inteiros não-negativos.")

    final_value = value
    if age >= 65:
        final_value *= 0.80
    if final_value > 100:
        final_value *= 0.90
    discount = value - final_value
    print(f"O valor final é R${final_value:.2f} ")

    shopping.append({"gross": value, "final": final_value, "discount": discount})

    gross_total += value
    discount_total += discount
    final_total += final_value

print("\n" + "=" * 30)
print(f"{'RESUMO DO PEDIDO':^30}")
print("=" * 30)
print(f"Quantidade de itens: {len(shopping):>9}")
print(f"Total Bruto:        R${gross_total:>8.2f}")
print(f"Total de Descontos: R${discount_total:>8.2f}")
print("-" * 30)
print(f"TOTAL A PAGAR:      R${final_total:>8.2f}")
print("=" * 30)
