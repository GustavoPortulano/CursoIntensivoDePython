print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("Página 141 - Percorrendo todas as chaves de um dicionário com um laço.")

print("\n")
favorite_languages = {'jen':'´python','sarah':'c','edward':'ruby','phil':'python'}

print("Criando uma lista com nomes que receberão uma mensagem.")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + " , I see your favorite language is +"
            "favorite_languages[name].title()")

print("\n")