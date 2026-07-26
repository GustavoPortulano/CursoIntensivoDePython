print("\n26 de julho de 2026. Domingo. Madrugada fria.")
print("Página 138 - Percorrendo todos os pares chave-valor com um laço.")
print("\n")

print("Primeiro exemplo:")
user_0 = {'username':'efermi','first':'enrico','last':'fermi', }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n-----------------------------------------------------------------------")

print("Segundo exemplo")

favorite_languages = {'jes':'python','sarah':'c','edward':'ruby','phil':'python'}

for name, language in favorite_languages:
    print(name.title() + " 's favorite laguage is " + language.title())

print("\n")