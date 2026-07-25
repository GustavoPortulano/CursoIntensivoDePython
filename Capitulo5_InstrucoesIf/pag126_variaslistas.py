print("\n24 de julho de 2026. Sexta-feira. Tarde fria e nublada.")
print("Página 126 - Usando várias listas.")
print("\n")

#lista de ingredientes:
available_toppings = ['mushrooms','pineapple','pepperoni','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n")