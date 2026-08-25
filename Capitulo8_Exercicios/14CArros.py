print("\n25 de agosto de 2026. Terça-feira. Tarde quente.")
print("8.14 - Carros: Escreva uma função que armazene informações sobre um carro" \
"\nem um dicionário. A função sempre deve receber o nome de um fabricante e um modelo." \
"\nUm número árbitrario de arugmentos nomeados estão deverá ser aceito. Chame a função" \
"\ncom as informações necessária e dois outros pares nome-valor, por exemplo, uma cor" \
"\nou um opcional. Sua função deve ser apropriada para uma chamdada como esta:" \
"\ncar = make_car('subaru','outback',color='blue',tow_package='True'). Mostre o " \
"\ndicionário devolvido para garantir que todas as informações forma armazenadas " \
"\ncorretamente.",)

def car(fabricante,modelo, **itens_carro):
    carro = {}
    carro['fabricante'] = fabricante.title()
    carro['modelo'] = modelo.title()
    for key, value in itens_carro.items():
        carro[key] = value
    return carro

make_car = car('subaru','outback',color= 'blue',tow_package=True )
print(make_car)