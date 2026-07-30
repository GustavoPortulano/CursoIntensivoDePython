print("\n29 de julho de 2026. Quarta-feira. Noite fria\n")

"""Cria uma lista vazia para armazenar 30 alienígenas:"""
aliens = []

"""Cria 30 alienígenas verdes:"""
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow', }
    aliens.append(new_alien)

"""Mostra os primeiros 5 alienígenas"""
for alien in aliens[:5]:
    print(alien)
print("...")

"""Mostra quantos aliens foram criados"""
print("Total nuber of aliens: " + str(len(aliens)) + "\n")
