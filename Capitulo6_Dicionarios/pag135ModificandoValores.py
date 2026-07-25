print("\n24 de julho de 2026. Sexta-feira. Noite nublada.")
print("Modificando valores.")

#Monitorando a posição de um alienígena que pode se deslocar com
#volocidades diferentes.

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))
#Move o alienígena para a direita.
#Determina a distãncia que o alienígena deve se deslocar de acordo cum sua 
#velocidade atual.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Fora do laço
#A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
