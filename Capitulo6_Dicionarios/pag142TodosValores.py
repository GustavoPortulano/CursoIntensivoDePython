print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("Página 142 - Percorrendo todos os valores de um dicionário" \
"com um laço.\n")

favorite_languages = {'jen':'python','sarah':'c','edward':'ruby',
                      'phil':'python'}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())