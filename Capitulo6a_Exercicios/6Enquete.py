print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("6.6 - Enquete: Utilize o código em favorit_language.py [página150]" \
"\n\t * Crie uma lista de pessoas que devam participar da enquete sobre a linguagem" \
"\nfavorita. Inclua alguns nomes que já esejamno diciconário e outros que não estão." \
"\n\t * Percorra a lista de pessoas que devem participar da enquete. Se elas já" \
"\ntiverem respondido à enquete, mostre uma mensagem agradescendo por" \
"\nresponder. Se ainda não participaram da enquete, apresene uma mensagem" \
"\nconvidando-as a responder.")

favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}

pesquisados = ['ana','phil','glaucia','edward','cintia']

for name in favorite_languages.keys():
    print(name.title())
    if name in pesquisados:
        print("Oi " + name.title() + " , vejo que sua linguagem favorita é " +
              favorite_languages[name].title() + "." )
    else:
        print("Oi " + name.title() + " , vejo que você ainda não participou "
        "\nde nossa pesquisa. Peço que contribua com nosso trabalho.")
