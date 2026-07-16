print("\n15 de julho de 2026 - Quarta-feira. Noite quente.")
print("4.10 - Fatias: Usando um dos programas que você escreveu neste capítulo," \
"\nacrescente várias linhas o final do programa que façam o seginte:" \

"\n\tExiba a mensagem Os três primeiros itens da lista são:. Em seguida, use uma" \
"\nfatia para exibir os três primeiros ites da lista desse programa.")

cubos = []
for cubo in range(1,11):
    cubo = cubo**3
    cubos.append(cubo)
print("Lista original:")
print(cubos)
print("Os três primeiros itens da lista são:")
print(cubos[:3])

print("\n-----------------------------------------------------------------------")

print("\n\tExiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir" \
"\ntrês itens do meio da lista.")

print("Os três termos do meio da lista são:")
print("Lista original:")
print(cubos)
print(cubos[4:7])

print("\n-----------------------------------------------------------------------")

print("\n\tExiba a mensagem Os três últimos itens da lista são:. Use uma fatia para" \
"\nexibir os três últimos itens da lista.")
print("Lista original:")
print(cubos)
print(cubos[7:])

print("\n")