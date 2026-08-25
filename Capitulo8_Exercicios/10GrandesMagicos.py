print("\n23 de agosto de 2026. Domingo. Tarde quente.")
print("8.10 - Grandes mágicos: Comece com uma cópia de seu programa do"
"\nExercício 8.9. Escreva uma função chamada make_great() que modifique a"
"\nlista de mágicos acrescentando a expressão o Grande ao nome de cada mágico. "
"\nChame show_magicians() para ver se a lista foi realmente modificada.")

def show_magician(magicos):
    for magico in magicos:
        print(magico)

def make_great(magicos):
    for nome_magico in magicos:
        grandes_magicos.append(f"{nome_magico} o Grande")
        print(nome_magico.title() + " o Grande")

"""Criação da lista para as chamads das funções."""
n_magicos = ['maligna','mestre dos magos','merlin','sauroman','gandalf']
grandes_magicos = []

print("\nLista original:")
show_magician(n_magicos)
print(n_magicos)
print("\nLista com a expressão 'o Grande':")
make_great(n_magicos)
print(grandes_magicos)




