print("\n24 de julho de 2026. Sexta-feira. Noite chuvosa.")
print("5.11 - Números ordinais: Númerosordinais indicam sua posição em uma lista" \
"\npor exemplo, 1s ou 2nd, em inglês. A maioria dos números ordinais nessa " \
"\nlíngua termina com th, exceto i, 2 e 3." \
"\n\t * Armazene os números de 1 a 9 em uma lista." \
"\n\t * Percorra a lista com um laço." \
"\n\t * Use uma cadeia if-elif-else no laço para exibir a terminação apropriada" \
"\npara cada número ordinal. Sua saída deverá conter 1st 2nd 3rd 4th ..., e cada" \
"\nresultado deve estar em uma linha separada.")

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    if numero == 1:
        print(f"{numero}" + "st")
    elif numero == 2:
        print(f"{numero}" + "nd")
    elif numero == 3:
        print(f"{numero}" + "rd")
    else:
        print(f"{numero}" + "th")

print("\n")