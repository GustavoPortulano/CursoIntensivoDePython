print("\n17 de julho de 2026. Sexta-feira. Noite muito fria.")
print("Usando vários blocos elif.")
print("\n")

print("Determinado se uma pessoa com mais de 65 anos está apta a receber um desconto.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" +str(price) + ".")
print("\n")

