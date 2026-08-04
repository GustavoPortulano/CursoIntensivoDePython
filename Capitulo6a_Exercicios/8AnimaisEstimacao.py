print("\n30 de julho de 2026. Quinta-feira. Noite fria.")
("6.8 - Animais de estimação: Crie vários dicionários, em que o nome de cada"
"\ndicionário seja o nome de um animal de estimação. Em cada dicionário, inclua"
"\no tipo de animal e o nome do dono. Armazene esses diconários em uma lista"
"\nchamada pets. Em seguida, percorra sua lista com um laço e, à medida que "
"\nfizer isso, apresente tudo que você sabe sobre cada animal de estimação.")

print("\n")

fremem = {'nome':'fremem',
          'especie':'cachorro',
          'raça':'pastor alemão',
          'dono':'gustavo', }

cherry = {'nome':'cherry',
          'especie':'cachorro',
          'raça':'vira-lata',
          'dono':'vitor', }

drogo = {'nome':'drogo',
        'especie':'gato',
         'raça':'siamês',
         'dono':'hendel', }

pets = [fremem, cherry, drogo]

for animal in pets:
    nome =      f"{animal['nome'].title()}"
    especie =   f"{animal['especie']}"
    raça =      f"{animal['raça']}"
    dono =      f"{animal['dono'].title()}"
    print(f"{"Nome do animal de estimação: "}{nome}")
    print(f"{"Espécie: "}{especie}")
    print(f"{"Raça: "}{raça}")
    print(f"{"Dono: " }{dono}\n")