print("\n21 de agosto de 2026. Sexta-feira. Noite agradável.")
("Página 180 - Devolvendo um dicionário.")

def build_person(first_name, last_name):
    """Devolve um diconário com informações sobre uma pessoa."""
    """O que aparece em branco será substituído por dados fornecidos."""
    person = {'first':first_name, 'last':last_name}
    return person

"""Chamada da função:"""
"""Fornecendo dados:"""
musician = build_person('jimi','hendrix')
"""Dicionário devolvido:"""
print(musician)