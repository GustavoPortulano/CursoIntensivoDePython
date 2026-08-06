print("\n05 de agosto de 2026. Quinta-feira. Noite fria.")
print("CAPITULO 7 - ENTRADA DE USUÁRIO E LAÇOS WHILE")
print("Página 155 - Programa que determina se uma pessoa tem altura suficiente para" \
"\nandar em uma montanha russa.")

"""A função int() converte strings em números inteiros."""
heigth = input("How tall are you,in inches?  ")
heigth = int(heigth)  

if heigth >= 36:
    print("\nYou're tall enough to ride!\n")
else:
    print("\nYou'll be able to ride when you´re a litte older.\n")