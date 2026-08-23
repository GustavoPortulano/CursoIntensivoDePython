print("\n22 de agosto de 2026. Sábado. Noite fria.")
print("Página 183 - Modificando uma lista em uma função.")

"""O código abaixo não usa funções."""
# Começa com alguns designs que devem ser impressos 
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
# Simula a impressão de cada design, até que não haja mais nenhum.
# Transfere cada design para completed_models após a impressão 
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impressão 3D a partir de design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados 
print("\nThe folowing models have been printed:")
for completed_model in completed_models:
    print(completed_model)