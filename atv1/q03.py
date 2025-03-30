valor = float(input("Digite o valor das mercadorias: "))
if valor > 500:
    imposto = (valor - 500) * 0.5
    print("Imposto: R$", imposto)
else:
    print("Sem imposto.")
