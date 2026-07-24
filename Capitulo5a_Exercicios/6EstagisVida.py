print("\n23 de julho de 2026. Quinta-feira. Noite fria")
print("5.6 - Estágios da vida: Escreva uma cadeia if-elif-else que determine o" \
"\nestágio da vida de uma pessoa. Defina um valor para a variável age e então:" \
"\n\tSe a pessoa tierpelo menos 2 anos, mas menos de 4 anos, mostre uma" \
"\nmensagem dizendo que ela é uma criança." \
"\n\tSe a pessoa tiver pelo mens 4 anos, mas menos de 13 anos, mostre uma" \
"\nmensagem dizendo que ela é um(a) garoto(a)." \
"\n\tSe a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma" \
"\nmensagem dizendo que ela é um(a) adolescente." \
"\n\tSe a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma" \
"\nmensagem dizendo que ela é adulta." \
"\n\tSe a pessoa tiver 65 anos ou mais, mostre uma mensagemdizendo que essa" \
"\npessoa é idosa.")
print("\n")

# Variável
age = 4

if 2 <= age < 4:
    print(f"Sua idade é de {age} anos. Você é uma criança.")
elif 4 <= age < 13:
    print(f"Sua idade é de {age} anos. Você é um(a) garoto(a).")


