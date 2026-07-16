print("\n15 de julho de 2026. Quarta-feira. Noite fria.")

print("4.11 - Minhas pizzas,suas pizzas: Comece com seu programa do exercício 4.1" \
"\n(página 97). Faça uma cópia da lista de pizza à lista original.")

pizzas = ['a moda','quatro queijos','napolitana']
for pizza in pizzas:
    print(pizza)
print("\n")
for pizza in pizzas:
    print("Gosto muito de comer pizza de " + pizza + " à noite com minhas filhas "
    "\ne esposa.")
print("\n")
friend_pizzas = pizzas[:]

print(f"As pizzas favoritas de meus amigos são {friend_pizzas}.")  

print("\n-----------------------------------------------------------------------")

print("\n\tAdicione uma pizza diferente à pizza friend_pizzas.")

friend_pizzas.append('frango')
print(friend_pizzas)

print("\n-----------------------------------------------------------------------")

print("\nProve que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas" \
"\nfavorias são:; em seguida, utilize um laço for para exibir a primeira lista. " \
"\nExiba a mensagem As pizzas favorias de meu amigo são:; em segida, utiliza" \
"\num laço for para exibir a segunda lista. Certifique-se de que cada pizza" \
"\nnova esteja armazenada na lista apropriada.")

pizzas = ['a moda','quatro queijos','napolitana']
print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

print("As pizzas favoritas de meu amigo são")
for pizza_amigo in friend_pizzas:
    print(pizza_amigo)

print("\n")