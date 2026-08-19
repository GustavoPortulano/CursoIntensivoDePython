print("\n11 de agosto de 2026. Terça-feria. Noite fria.")
print("Argumentos posicionais.")

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
"""`Página 172 - Várias chamadas de função"""
"""Descrevendo um animal diferente."""
describe_pet('dog','wille')
print("\n")