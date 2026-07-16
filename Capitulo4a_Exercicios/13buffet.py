print("\n16 de julho de 2026. Quinta-feria. Inicio de madrugada fria.")
print("4.13 - Buffet: Um restaruante do tipo buffet oferece apenas cinco tipos básicos" \
"\nde comida. pense em cinco pratos simles e armazens-os em uma tupla.")

cardapio = ('peixada','feijoada','tropeiro','churrasco','carne de panela')
print(cardapio)
print("\n-----------------------------------------------------------------------")


print("\n\ttUse um laço for para exibir cada prato oferecido pelo restarurante.")

for prato in cardapio:
    print(prato)

print("\n-----------------------------------------------------------------------")
print("\n\tTente modificar um dos itense certifique-se de que Pyton rejeita a mudança.")

cardapio = ('peixada','feijoada','tropeiro','churrasco','carne de panela')

cardapio(0) = 'frango com pequi'

print("\n-----------------------------------------------------------------------")

print("\n\tO restaurante muda seu cardápio,substituindo dois dos itens com pratos" \
"\ndeferentes. Acrescente um bloco de código que reescreva a tupla e, em " \
"\nseguida, use um laço for para exibir cada um dos itens do cardápio" \
"\nrevisado.")

cardapio = ('peixada','feijoada','salada americana','churrasco','frango com pequi')
print("Novo cardápio:")
for prato in cardapio:
    print(prato)

print("\n")