print("\n06 de agosto de 2026. Quinta-feira. Inicio de madrugada.")
print("CAPITULO 7 - ENTRADA DE USUÁRIO E LAÇOS WHILE")
print("Página 156 - Múltiplos de dez: Peça um número ao usuário e, em  seguiida," \
"\ninforme se o númermo é múltiplo de dez ou não.\n")

numero = input("Digite um número inteiro: ")

numero = int(numero)

if numero % 10 == 0:
    print(f"O número {numero} é múltiplo de dez.")
else:
    print(f"O número {numero} não é múltiplo de dez.")

print("\n")