print("\n25 de agosoto de 2026. Terça-feira. Madrugada fria.")
print("Página 188 - Misturando argumentos posicinais e arbitrários.")

def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(("- " + topping))

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')