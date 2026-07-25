print("\n24 de julho de 2026. Sexta-feira. Tarde fria e nublada.")
print("5.9 - Sem usuários: Acrescente um teste if em hello_admin.py para garantir" \
"\nque a lista de usuarios não esteja vazia." \
"\n\tSe a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns" \
"\nusuários!" \
"\n\tRemova todos os nomes de usuário de sua lista e certifique-se de que a " \
"\nmensagem correta seja exibida.")

print("\n")


usuarios = []

#Representando uma lista vazia, mostrando que o nr de usuários é zero.
if len(usuarios) == 0:    
        print("A lista está vazia. Precisamos encontrar alguns usuários!")

for usuario in usuarios:
    if usuario == 'admin':
        print("Olá " + usuario.title() + ", gostaria de ver um relatório de status?")
    elif usuario != 'admin':
        print("Olá " + usuario.title() + ", obrigado por fazer login novamente.")

print("\n")
      
