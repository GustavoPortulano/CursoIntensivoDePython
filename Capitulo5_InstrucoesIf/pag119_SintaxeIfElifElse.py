print("\n17 de julho de 2026. Sexta-feira. Noite muito fria.")
print("Página 119 - Sintaxe if-elif-else.")
print("\n")

print("O códio a seguir testa a faixa etária de uma pessoa e então exibe uma mensagem" \
"\ncom o preço da entrada para o parque de diversões.")

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 10:
    print("Your adimission cost is $5.")
else:
    print("Your admission cost is $10.")
print("\n")

print("\nEm vez de exibir o preço da entrada no bloco if-elif-else, seria mais" \
"\nconciso apenas difinir o preço na cdeia if-elif-else e, então, ter uma instrução" \
"\nprint simples que execute depois que a cadeia for avaliada.")

if age < 4: 
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" +str(price) + ".")
print("\n")