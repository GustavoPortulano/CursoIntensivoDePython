print("n13 de julho de 2026. Segunda-feira. Noite fria")
print("4.2 - Animais: Pense em pelo menos três animais diferentes que tenham uma" \
"\ncaracterística em comum. Armazene os nomes desses animais em uma lista e," \
"\nentão, utilize um laço for para exibir o nome de cada animal")

animais = ['onça','pantera','jaguatirica']
for animal in animais:
    print(animal)

print("\n-----------------------------------------------------------------------")

print("\nModifique seu programa para exibir uma frase sobre cada animal, por "
"\nexemplo,Um cachorro seia um ótimo animal de estimação.")
for animal in animais:
    print("A " + animal + " não é um animal domesticável.")

print("\n-----------------------------------------------------------------------")

print("\nAcrescente uma linha no final de seu programa informando o que esses " \
"\nanimais tê em comum. Você poderia exibir uma frase como Qualquer um " \
"\ndesses animais seria um ótimo animal de estimação.")

print("\n")
for animal in animais:
    print("A " + animal + " não é um animal domesticável.")
print("Todos os animais listados são felinos selvagens.")

print("\n")