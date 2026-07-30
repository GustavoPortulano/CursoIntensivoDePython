print("\n30 de julho de 2026. Quinta-feira. Madrugada fria.")
print("Pagina 146 - Uma lista em um dicionário.\n")

#Armazena informações sobre uma pizza que está sendo pedida.
pizza = {'crust':'thick','toppings':['mushrooms','extra cheese'], }
#Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

print("\n")
