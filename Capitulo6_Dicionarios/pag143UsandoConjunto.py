print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("Página 143 - Exibindo um conjunto de valores sem repetições usando "
"\num conjutno set().")

favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
