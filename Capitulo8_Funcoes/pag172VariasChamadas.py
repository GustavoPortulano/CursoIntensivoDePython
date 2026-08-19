print("18 de agosto de 2026. Terça-feira. Noite fria.")
print("Página 172 - Várias chamadas de função.")

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
