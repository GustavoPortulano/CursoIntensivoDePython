print("\n24 de agosto de 2026. Segunda-feira. Noite fria.")
print("Página 187 - Passando um número arbitrário de argumentos.")

def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos;"""
    print(toppings)

print("Listas de ingredientes:")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')