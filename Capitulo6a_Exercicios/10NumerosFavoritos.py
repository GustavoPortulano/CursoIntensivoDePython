print("\n05 de agostos de 2026. Quarta-feira. Noite fresca.")
print("6.10 - Números favoritos: Modifique o seu programa do Exercício 6.2 (página" \
"\n147) para que cada pessoa possa ter mais de um número favorito. Em seguida, " \
"\napresente o nome de cada pessoa, juntamente com seus números favoritos.\n")

numeros_favoritos = {'ana':{654,54,645,245, },
                     'clara':{64,5461,12,0, },
                     'dimitry':{631,254,951,6, },
                     'maria':{49,410,351,23, },
                     'denize':{954,321,25,650,0, }}

#Uso do laço for para exibir o nome e o número,
#numero representa a chave (nome),
#numeros_favoritos[numero] tem como saida o valor (número),
#f{ } permite exibir strings e números no mesmo testo.

for nome, numeros in numeros_favoritos.items():
    print("Os números favoritos de " + nome.title() + " são:")
    for numero in numeros:
        print("\t" + f"* {numero}")
          

print("\n")

