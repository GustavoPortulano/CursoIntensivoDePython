print("\n25 de agosto de 2026. Terça-feira. Tarde quente.")
print("8.12 - Sanduíches: Escreva uma função que aceite uma lista de itens que uma" \
"\npessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe" \
"\ntantos itens quantos forem fornecidos pela chamada da função e deve" \
"\napresentar um resumo do sanduíche pedido. Chame a função três vezes usando" \
"\num número diferente de argumentos a cada vez.")

def make_sanduiches(*ingredientes):
    print(ingredientes)

make_sanduiches('ovo')
make_sanduiches('ovo','presunto','mussarela')
make_sanduiches('salsicha','molho','purê de batata','passas','batata palha','maioneze')