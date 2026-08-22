print("\n21 de agosto de 2026. Terça-feira. Noite agradável")
print("Página 181 - Usando uma função com um laço while.")

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name 
    return full_name.title()

    # Este é um loop infinito.
while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name: ")
    l_name = input("Last_name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
