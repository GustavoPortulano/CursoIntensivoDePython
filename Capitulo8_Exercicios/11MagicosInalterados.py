print("\n23 de agosto de 2026. Domingo. Noite fria.")
print("8.11 - Mágicos inalterados: Comece com o trabalho feito no exercício 8.10." \
"\nChame a função make_great() com uma cópia da lista de nomes de mágicos. Como a" \
"\nlista original não será alterada, devolva a nova lista e armazene-a em uma " \
"\nlista serparada. Chame show_magicians() com cada lista para mostar que você" \
"\ntem uma lista de nomes originais e uma lista com a expressão o Grande adicionada" \
"\nao nome de cada mágico.")

"""Definindo a lista:"""
n_magicos = ['merlyn','maligna','gandalf']
grandes_magicos = []

def show_magicians(nomes_de_magicos):
    """Lista = nomes_de_magicos."""
    for nome_de_magico in nomes_de_magicos:
        print(nome_de_magico.title())

def make_great(nomes_de_magicos):
    for nome_de_magico in nomes_de_magicos:
        grandes_magicos.append(f"{nome_de_magico}  o Grande")
    return grandes_magicos

"""Copiando a lista e salvando-a em uma variável:"""
gd_magicos = make_great(n_magicos[:])

print("Lista original:")
show_magicians(n_magicos)
print("\n")
print("Exibindo a lista como a expressão 'o Grande':")
show_magicians(gd_magicos)

print("\nNome do mágico seguido da expressão 'o Grande'.")
print(gd_magicos)
print("Lista original.")
print(n_magicos)








