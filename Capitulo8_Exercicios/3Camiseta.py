print("\n18 de agosto de 2026. Terça-feira. Noite fria.")
print("Exercício 8.3 - Camiseta: Escreva uma função chamada make_shirt() que aceite um" \
"\n tamanho e o texto de uma mensagem que deverá ser estampada na camiseta." \
"\nA função deve exibir uma frase que mosre o tamanho da camiseta e a " \
"\nmensagem estampada." \
"\n\tChame a função uma vez usando argumentos posicionais para criar uma" \
"\ncamiseta. Chame a função uma segunda vez usando argumentos nomeados.")

def make_shirt(tamanho_camiseta, texto_camiseta):
    print("Tamanho da camiseta: " + tamanho_camiseta + ".")
    print("Texto: " + texto_camiseta + "." )

print("\nUsando argumentos posicionais:")
make_shirt('G', 'Análise Estatístcia com Excel')
print("Usando argumentos nomeados:")
make_shirt(tamanho_camiseta='M', texto_camiseta='Curso Intensivo de MySQL')