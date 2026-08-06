print("\n06 de agosto de 2026. Quinta-feira. Inicio de madrugada.")
print("CAPITULO 7 - ENTRADA DE USUÁRIO E LAÇOS WHILE")
print("Página 156: Lugares em um restaurante: Escreva um programa que pergunte ao usuário" \
"\nquantas pessoa estão em seu grupo para jantar. Se a resposta for maior que " \
"\noito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso" \
"\ncontrário, informe que sua mesa está pronta.\n")

lugares = input("Bom dia! Quantas pessoas então em seu grupo de jantar? ")

lugares = int(lugares)

if lugares > 8:
    print("Para um número de convidados maior que oito, pedimos que esperem por uma mesa.")
else:
    print("Sua reserva de mesa está confirmada.")

print("\n")