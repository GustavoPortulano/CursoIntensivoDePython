print("\n24 de julho de 2026. Sexta-feira. Tarde fria e nublada.")
print("5.8 - Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo" \
"\no nome admin. Suponha que você esteja escrevendo um código que exibirá" \
"\numa saudação a cada usuário depois que eles fizerem login em um site." \
"\nPercorra a lista com um laço e mostre uma saudação para cada usuário." \
"\n\tSe o nome do usuário for admin, mostre uma saudação especial, por exemplo," \
"\nOlá admin, gostaria de ver um relatório de status?" \
"\n\tCaso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por" \
"\nfazer login novamente.")
print('\n')

usuarios = ['ana','paula','pedro','admin','joão','maria']

for usuario in usuarios:
    if usuario == 'admin':
        print("Olá " + usuario.title() + ", gostaria de ver um relatório de status?")
    elif usuario != 'admin':
        print("Olá " + usuario.title() + ", obrigado por fazer login novamente.")

print("\n")