print("\n20 de agosto de 2026. Quinta-feira. Madrugada fria.")
print("Página 178 - Deixando um argumento opcional.")

"""Acrescentando o nome do meio."""
def get_formatted_name(first_name, middle_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musicisan = get_formatted_name('john', 'lee', 'hooker')
print(musicisan)