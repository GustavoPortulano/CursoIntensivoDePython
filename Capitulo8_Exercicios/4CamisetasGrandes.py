print("\n18 de agosto de 2026. Terça-feira. Noite fria.")
print("8.4 - Camisetas grandes: Modifique a função make_shirt() de modo que as " \
"\ncamisetas sejam grades por default, com uma mensagem Eu amo Python. Crie" \
"\numa camiseta grande e outra média coma a mensagem default, e uma camiseta" \
"\nde qualquer tamanho com uma mensagem diferente.")

def make_shirt(tamanho_camiseta='G', texto_camiseta='Eu amo Python'):
    print("Tamanho da camiseta: " + tamanho_camiseta + ".")
    print("Texto da camiseta: " + texto_camiseta + ".")

print("Camiseta com tamanho e texto padrões.")
make_shirt()
print("Camiseta com tamanho e texto diferentes do padrão.")
make_shirt('M', 'Cibersegurança')
