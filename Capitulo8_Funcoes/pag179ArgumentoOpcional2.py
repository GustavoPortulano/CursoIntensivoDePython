print("\n20 de agosto de 2026. Quinta-feira. Madrugada fria.")
print("Página 179 - Deixando um argumento opcional.")


"""O argumento opcional é o último parâmentro."""
"""Ele deve receber um valor vazio (='')"""
"""Neste exemplo, o valor opconal é o nome do meio."""

def get_formated_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    """Usando IF;"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)
musician = get_formated_name('jimi', 'hooker', 'lee')
print(musician)