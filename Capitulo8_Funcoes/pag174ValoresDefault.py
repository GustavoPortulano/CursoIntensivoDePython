print("\n18 de agosto de 2026. Terça-feira. Noite fria.")
print("Página 174 - Valores default.")

def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
"""Especificando um argumento para o parâmetro animal_type:"""
describe_pet(pet_name='harry', animal_type='hamster')