print("\n24 de agosto de 2026. Segunda-feira. Noite fria")
print("Utilizando um laço:")

def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(" - " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')