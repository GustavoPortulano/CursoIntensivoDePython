print("\n12 de julho de 2026. Domingo, tarde fria")
print("3.6 - Mais convidados: Você acabou de encontrar uma mesa de jantar maior,"
"\nportando agora tem mais espaço disponível. Pense em mais três convidados"
"\npara o jantar."
"\n------------------------------------------------------------------------")
print("Comece com seu programa do Exercício 3.4. Acrescente" \
"\numa instrução print no final de seu programa informando às pessoa que" \
"\nvocê encontrou uma mesa de jantar maior." 
"\n------------------------------------------------------------------------")
print("Utilize insert() para adicionar um novo convidado no início de sua lista;" \
"\nutilize insert() para adicionar um novo convidado no meio de sua lista;" \
"\nutilize insert() para adicionar um novo convidade no final de sua lista." \
"\n------------------------------------------------------------------------")
print("Exiba um novo conjunto demensagens de convite,uma para cada pessoa que " \
"\nestá em sua lista." \
"\n------------------------------------------------------------------------")

print("1 - Informando que foi encontrada uma mesa maior:")
convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']
primeiroconvidado = convidados.pop()
segundoconvidado  = convidados.pop()
terceiroconvidado = convidados.pop()
print( primeiroconvidado + " , bom dia. Encontrei uma mesa maior e, assim sendo, teremos mais convidados.")
print( segundoconvidado  + " , bom dia. Encontrei uma mesa maior e, assim sendo, teremos mais convidados.")
print( terceiroconvidado + " , bom dia. Encontrei uma mesa maior e, assim sendo, teremos mais convidados.")
print("\n------------------------------------------------------------------------------")

print("Acrescentando novos convidados à lista:")
convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']
print("Lista original:")
print(convidados)
print("Acrescentando novo convidado ao início da lista:")
convidados.insert(0, 'Marie Curie')
print(convidados)
print("Acrescentando novo convidado no meio da lista:")
convidados.insert(2, 'Isaac Asimov')
print(convidados)
print("Acrescentando novo convidado ao final da lista:")
convidados.insert(5, 'João Candido')
print("Lista final de convidados:")
print(convidados)

print("\n------------------------------------------------------------------------")

print("Enviando convites aos convidados:")

convidados = ['Marie Curie', 'D. Pedro II', 'Isaac Asimov', 'Machado de Assis', 'Teodósia','João Candido']
convidado1 = 'Marie Curie'
convidado2 = 'D Pedro II'
convidado3 = 'Isaac Asimov'
convidado4 = 'Machado de Assis'
convidado5 = 'Teodosia'
convidado6 = 'João Candido'

print(convidado1 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(convidado2 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(convidado3 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(convidado4 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(convidado5 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(convidado6 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")

print("\n")
