print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\n7.4 - Ingredientes para uma pizza: Escreva um laço que peça ao usuário para" \
"\nfornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja" \
"\nfornecido. À medida que cada ingrediente é especificado, apresente uma mensagem" \
"\ninformando que você acrescentará esse ingrediente à pizza.")

prompt = "\nDigite um ingredite para preparar sua pizza."
prompt += "\nO ingrediente pedido será acrescentado. "

"""Usando uma flag."""
"""Primeiro é definido o valor de entrada do laço como verdadeiro."""
ativo = True

while ativo:
    mensagem = input(prompt)
    if mensagem == 'quit':
        ativo = False
    else:
        print(mensagem)

print("\n")

