print("\n10 de agosto de 2026 - Segunda-feira. Noite fresca.")
print("7.10 - Férias dos sonhos: Escreva um programa que faça uma enquete sobre as " \
"\nférias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse" \
"\nvisitar um lugar do mundo, para onde você iria? Inclua um bloco de código que " \
"\napresente os resultados da enquete.")

print("\n")

continua = True


resultados_enquete = []

while continua:
    prompt = input("Se pudesse visitar um lugar do mundo, para onde você iria?  ")
    resultados_enquete.append(prompt.title())
    prompt2 = input("Finalizar pesquisa (sim/não)? ")
    if prompt2 == 'sim':
        continua = False
    if prompt2 != 'sim' and prompt2 != 'não':
        print("Resposta incorreta. Digite apenas 'sim' ou 'não'.")

print("\nResultados da pesquisa:")
print(resultados_enquete)
   

    


