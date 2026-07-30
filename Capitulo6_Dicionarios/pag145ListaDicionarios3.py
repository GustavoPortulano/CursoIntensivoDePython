print("\n29 de julho de 2026. Quinta-feira. Madrugada fria.")

print("Fazer com que alguns alienígenas mudem de cor e velocidade.")
# Criar uma lista vazia para armazenar os alienígenas.
aliens = []
# Criar 30 aliens verdes.
for alien in range(0,30):
    new_alien = {'color':'green','points':5,'spees':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Mostra os 5 primeiros alienígenas
for alien in aliens[0:5]:
    print(alien)
print("...")
print("\n")

