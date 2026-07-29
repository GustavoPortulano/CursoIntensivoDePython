print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("Página 141 - Percorrendo as chaves de um dicionário " \
"\nem ordem usando um laço usando a função sorted().\n")

print("Percorrendo todas a chaves usadno um laço:")
favorite_languages = {'jen':'´python','sarah':'c','edward':'ruby','phil':'python'}

for name in sorted(favorite_languages.keys()):
    print(name.title() + " ,"
    "thank you for takin the poll.")

print("\n")