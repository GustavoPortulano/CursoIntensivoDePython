print("\n09 de agosto de 2026. Domingo. Tarde normal.")
print("\nPágina 165 - Preenchendo um dicionário com dados de entradas do usuário.")

responses = {}
# Define uma flag par aindicar que a enquete está ativa

polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = input("\nWhat is your name: ")
    response = input("Which mouch wold you like to climb someday? ")
    # Armazena a respost ano dicionário
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        # A enquete foi concluída
    print("\n --- Poll Results ---")
    for name, response in responses.items():
        print(name.title() + " Would like to climb " + response.title() + ".")
