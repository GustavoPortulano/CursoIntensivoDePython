print("\n13 de julho de 2026 - Segunda-feria. Noite fria.")
print("4.1 - Pizzas: Pense em pelomenso três tipos de pizzas favoritas. Armazene os" \
"\nnomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada" \
"\npizza.")

pizzas = ['a moda','quatro queijos','napolitana']
for pizza in pizzas:
    print(pizza)

print("\n-----------------------------------------------------------------------")

print("\nModifique seu laço for para mostar uma frase usando o nome da pizza em" \
"\nvez de exibir apenas o nome dela. Para cada pizaa, você deve ter uma linha" \
"\nna saída contendo uma frase simples como Gosto de pizza de pepperoni.")
print("\n")
for pizza in pizzas:
    print("Gosto muito de comer pizza de " + pizza + " à noite com minhas filhas e esposa.")


