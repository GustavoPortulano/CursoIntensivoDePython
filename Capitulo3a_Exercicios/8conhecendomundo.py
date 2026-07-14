print("\n3.8 - Conhecendo o mundo: Pense em pleo menos cinco lugares do mundo que" \
"\n você gostaria de visitar.")

print("\nArmazene as localidades em uma lista. Certifique-se de que a lista não esteja" \
"\nem ordem alfabética.")
localidades = ['parque do peruaçu','ouro preto','são joão del rey','india','portugal']
print("\n-----------------------------------------------------------------------")

print("Exiba sua lista na ordem original. Não se preocupe em exibir a lista de " \
"\nforma elegante; basta exibi-la como uma lista Python pura.")
print(localidades)
print("\n------------------------------------------------------------------------")

print("Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a" \
"\nlista propriamente dita.")
print(sorted(localidades))
print("\n------------------------------------------------------------------------")

print("Mostre que sua lista manteve sua ordem original exibindo-a")
print(localidades)
print("\n------------------------------------------------------------------------")

print("Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar" \
"\n a ordem da lista original")
print(sorted(localidades, reverse=True))
print("\n------------------------------------------------------------------------")

print("Mostre que sua lista manateve sua ordem original exibindo-a novamente.")
print(localidades)

print("\n------------------------------------------------------------------------")

print("Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar" \
"\nque sua ordem mudou")
localidades.reverse()
print(localidades)
print("\n------------------------------------------------------------------------")

print("Utilize reverse() para mudar a ordem de sua lista novamene. Exiba a lista" \
"\npara mostar que ela voltou à sua ordem original.")
localidades.reverse()
print(localidades)
print("\n------------------------------------------------------------------------")

print("Utilize sort() para mudar sua lista de modo que ela seja armazenada em" \
"\nordem alfabética. Exiba a lista para mostar que sua ordem mudou.")
localidades.sort()
print(localidades)
print("\n------------------------------------------------------------------------")

print("Utilize sort() para mudarsua lista de modo que ela seja armazenada em " \
"\nordem alfabética inversa. Exiba a lista para mostar que sua ordem mudou.")
localidades.sort(reverse=True)
print(localidades)
print("\n------------------------------------------------------------------------")