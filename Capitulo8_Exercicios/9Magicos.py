print("\n23 de agosto de 2026. Domingo. Tarde quente.")
print("8.9 - Mágicos: Crie uma lista de nomes de mágicos. passe a lista para uma" \
"\nfunção chamada show_magicians() que exiba o nome de cada mágico da lista.")

def show_magicians(nomes_de_magicos):
    """Lista = nomes_de_magicos."""
    for nome_de_magico in nomes_de_magicos:
        nomes = nome_de_magico
        print(nomes.title())
        

"""Definindo a lista e inserindo nomes dos mágicos:"""
n_magicos = ['maligna','mestre dos magos','merlin','sauroman','gandalf']
"""Chamando a função:"""
print("Mágigos citados na lista:")
show_magicians(n_magicos)
"""Exibindo a lista criada."""
print("Lista criada:")
print(n_magicos)
