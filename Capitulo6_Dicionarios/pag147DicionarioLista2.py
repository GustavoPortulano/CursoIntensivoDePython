print("\n30 de julho de 2026.Quinta-feira. Madrugada fria.")
print("Uma lista em um dicionário.")

favorite_languages = {'jen':['python','ruby'],'sarah':['c'],
                      'edward':['ruby','go'],'phil':['python','haskell'], }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "s' favorite languages are:")
    for language in languages:
        print("\t" + language.title())

print("\n")