print("\n24 de julho de 2026. Sexta-feira. Início de madrugada fria.")

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#Se a pizza ficar sem pimentões verdes, é usado uma instrução if no
#laço for para esta situação.

print("\n")

for requested_topping in requested_toppings:
    if requested_topping ==  'green peppers':
        print("Sorry, we are out of grenn peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n")
