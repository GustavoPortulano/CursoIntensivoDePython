print("\n11 de agosto de 2026. Terça-feira. Noite fria")
print("8.2 - Livro favorito: Escreva uma funão chamada favorite_book() que aceite" \
"\num parâmetro title. A função deve exibir uma mensagem com Um dos meus " \
"\nlivros favoritos é Alice no país das maravilhas. Chame a função e nã ose" \
"\nesqueça de incluir o título do livro como argumento na chamada da função.\n")

def favorite_book(livro):
    print("Meu livro favorito é " + livro.title() + ".")

favorite_book('duna')
favorite_book('o conde de monte cristo')
favorite_book('1984')
favorite_book('os sinos da agonia')

print("\n")