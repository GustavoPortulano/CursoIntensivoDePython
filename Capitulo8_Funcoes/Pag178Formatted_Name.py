print("\n20 de agosto de 2026. Quinta-feira. Madrugada fria.")
print("Página 177 - Valores de retorno.")
print("Página 178 - Devolvendo um valor simples.")

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('elis', 'regina')
print(musician)