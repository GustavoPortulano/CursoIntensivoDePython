print("\n30 de julho de 2026. Quinta-feira. Noite fria.")
print("6.9 - Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em" \
"\ntrês nomes para usar como chaves do dicionário e armazene de um a três" \
"\nlugares favoritos para cada pessoa. Percorra o dicionário com um laço e apresente" \
"\n o nome de cada pessoa e seus lugares favoritos.\n")

favorite_places = {'vilma':['praia','sítio'],
                   'beth':['shopping','praia','clube'],
                   'gean':['clube','estádio','sitio']}

"""Nomeando a chave como NOME  e o valor como LUGARES, o dicionário fica dividido
em duas partes, que são trabalhadas de forma independente em cada laço FOR."""

for nome, lugares in favorite_places.items():
    print(f"Os lugares favoritos de {nome.title()} são:")
    for lugar in lugares:
        print("\t" + f"*{lugar}")

print("\n")
    


    