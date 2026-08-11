print("\n10 de agosto de 2026. Segunda-feira. Noite normal.")
print("7.8 - Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com" \
"\nos nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada" \
"\nfinished_sandwiches. Percorra a list ade pedidos de sanduíches com um laço e" \
"\nmostre uma mensagempara cada pedido, por exemplo, Preparei seu" \
"\nsanduíche de atum. À medida que cada sanduíche for preparado, transfira-o" \
"\npara a lista de sanduíches prontos. Depois que todos os sanduíches estiverem" \
"\nprontos, mostre uma mensagem que liste cada sanduíche preparado.")

print("\n")

sandwich_orders = ['atum','misto-frio','hamburguer','cachorro-quente','x-tudo']
finished_sandwiches = []

while sandwich_orders:
    sanduiche_finalizado = sandwich_orders.pop()
    print("Verificando a finalização do sanduíche: " + sanduiche_finalizado)
    finished_sandwiches.append(sanduiche_finalizado)
    #Exibe todos os sanduíches finalizados.
    print("O " + sanduiche_finalizado + " esta pronto.")
    print("Relação de sanduíches prontos.")
    print(finished_sandwiches)
    print("\n")

