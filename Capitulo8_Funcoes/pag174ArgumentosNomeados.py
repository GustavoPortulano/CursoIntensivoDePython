print("\n18 de agosto de 2026. Terça-feira. Noite fria.")
print("Página 173 - Argumentos nomeados.")

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet(animal_type='hamster', pet_name='harry')