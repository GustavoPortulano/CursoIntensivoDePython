print("\n21 de agosto de 2026. Sexta-feira. Noite agradável.")
print("Segundo exemplo.")

def build_person(first_name, laste_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first':first_name,   'last':laste_name}
    if age:
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)