print("\n25 de julho de 2026. Noite fria.")
print("6.2 - Númermos favoritos: Use um dicionário ppara armazenar os números favoritos" \
"\nde algumas pessoas. Pense em cinco nomes e use-os como chaves em seu dicionário. " \
"\nPense em um número favorito para cada pessoa e armazene cada um como um valor" \
"\nem seu dicionário. Exiba o nome de cada pessoa e seu número favorito.")

numeros_favoritos = {'ana':654,'clara':64,'dimitry':631,
                    'maria':49,'denize':954,}

#Uso do laço for para exibir o nome e o número,
#numero representa a chave (nome),
#numeros_favoritos[numero] tem como saida o valor (número),
#f{ } permite exibir strings e números no mesmo testo.

for numero in numeros_favoritos:
    print("O número favorito de " + numero.title() + 
          f" é {numeros_favoritos[numero]}.")

print("\n")
   