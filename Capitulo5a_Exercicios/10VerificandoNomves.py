print("\n24 de julho de 2026. Sexta-feira. Noite fria.a")
print("5.10 - Verificando nomes de usuarios? Faça o seguinte para criar um programa" \
"\nque simule o modo como os sites garantesm que todos tenham um nome de " \
"\nusuário único." \
"\n\t * Crie uma lista chamada current_users com cinco ou mais nomes de usuários." \
"\n\t * Crie outra lista chamada new_users com cinco nomes de usuários. Garanta " \
"\n\tque um ou dois dos novos usuários também estejam na lista currente_users." \
"\n\t * Percorra a lista new_users com um laço para ver se cada novo nome de" \
"\nusuário já foi usado. Em caso afirmativo, mostre uma mensagem informando" \
"\nque a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi" \
"\nusado, apresente uma mensagem dizendo que o nome do usuário está disponível." \
"\n\t * Certifique-se de que sua comparação não levará em conta as diferenças" \
"\nentre letras maiúsculas e minúsculas. Se John foi usado, JOHN não deverá " \
"\nser aceito.")

print('\n')

current_users = ['ana','Bela','paulo','mateus','sergio','marta','denise','mateus']
new_users = ['ana','bela','cintia','clyon','dermezel','Marta','MATEUS']

#Torna os itens da lista current_users em letras minúsculas.
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    #Torna os intens da lilsta new_users em letras minúsculas.
    if new_user.lower() in current_users_lower:
        print(f'O nome "{new_user.title()}" já foi usado. Você precisa digitar um novo nome.')
    else:
        print(f'O nome "{new_user.title()}" está disponível.')

print("\n")