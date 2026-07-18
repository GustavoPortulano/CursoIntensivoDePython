print("\n17 de julho de 2026. Sexta-feira. Noite muito fria.")
print("Cores de alienígenas #1: Suponha qu um alienígena acabou de ser" \
"\natingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um" \
"\nvalor igual a green, yellow ou red.")
print("\n\tEscreva uma instrução if para testar se a cor do alienígena é verde. Se for," \
"\nmostre uma mensage informando que o jogador acabou de ganhar cinco pontos")

alien_color = 'red'
if alien_color is 'green':
    print("Parabéns, a cor do alienígena é verde. Você ganhou 5 pontos.")
else:
    print(f"A cor do alienígena não é green, é {alien_color}.")
    print("Você não pontuou.")

print("\n\tEscreva uma versão desse programa em que o teste if passe e outro em que" \
"\nele falhe. (A versão que falha não terá nenhuma saída.)")

alien_color = 'green'
if alien_color is 'green':
    print(f"A cor do alienígena é {alien_color}. Você ganhou 5 pontos.")
if alien_color is 'red':
    print(f"A cor do alienígena é {alien_color}.")

print("\n")