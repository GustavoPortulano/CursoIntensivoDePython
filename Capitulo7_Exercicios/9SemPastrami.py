print("\n10 de agosto de 2026. Segunda-feira. Noite normal.")
print("7.9 - Sem pastrami: Usando a lista sandwich_orders do Exercicio 7.8, garanta" \
"\nque o sanduíche de pastrami apareça na lista pelo menos três vezes. Acrescente" \
"\num código próximo ao início de seu programa para exibir uma mensagem informando" \
"\nque a lanchonete esta sem pastrami e, então, use um laço while para remover todas" \
"\nas ocorrências de pastrami em sandwich_orders. Garanta que nenhum sanduíche de" \
"\npastrami acabe em finished_sandwiches.")

sandwich_orders = ['atum','misto-frio','pastrami',
                   'pastrami','hamburguer','cachorro-quente',
                   'x-tudo','pastrami','bauru']
finished_sandwiches = []

print("\nSenhores clientes! Informamos que hoje estamos sem pastrami e" \
"\ndesta forma todas as opções em nosso cardápio que contarem este ingrediente" \
"\nnão estarão disponíveis.")

print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

print("\n--------------------")

while sandwich_orders:
    sanduiche_finalizado = sandwich_orders.pop()
    print("Verificando a finalização do sanduíche: " + sanduiche_finalizado)
    finished_sandwiches.append(sanduiche_finalizado)
    #Exibe todos os sanduíches finalizados.
    print("O " + sanduiche_finalizado + " esta pronto.")
    print("Relação de sanduíches prontos.")
    print(finished_sandwiches)
    print("\n")