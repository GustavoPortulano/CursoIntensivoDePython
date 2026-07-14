print("\n13 de julho de 2026. Segunda-feria. Noite fria.")
print("Página 89 - Executando mais tarefas em um laço for.")
print("\n")
magicians = ['alice','david','carolina']

for magician in magicians:
    print(magician.title() + " , that was a grat trick!")

print("\n-------------------------------------------------------------")

print("\nAcrescentando uma segunda linha à mensagem:")
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + " , that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("\n")