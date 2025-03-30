dias = int(input("Quantidade de dias: "))
km = float(input("Quilômetros rodados: "))

custo = dias * 90

if km > 100:
    custo += (km - 100) * 12
print("Custo total: R$", custo)
