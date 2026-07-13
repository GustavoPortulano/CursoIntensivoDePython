print("\n12 de julho de 2026. Domingo, noite fria, choveu um pouco.")
print("3.7 - Reduzindo a lista de convidados: Você acabou de descobrir que sua nova" \
"\nmesa dejantar não chegará a tempo para o jantar e tem espaço para somente" \
"\ndois convidados.")

print("\nComece com seu programa do Exercício 3.6. Acrescente uma nova linha que" \
"\nmostre uma mensagem informando que você pode convidar apenas duas " \
"pessoas para o jantar.")

print("\n-----------------------------------------------------------------------")
convidados = ['Marie Curie', 'D. Pedro II', 'Isaac Asimov', 'Machado de Assis', 'Teodósia','João Candido']
convidado1 = 'Marie Curie'
convidado2 = 'D Pedro II'
convidado3 = 'Isaac Asimov'
convidado4 = 'Machado de Assis'
convidado5 = 'Teodosia'
convidado6 = 'João Candido'

print(convidado1 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")
print(convidado2 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")
print(convidado3 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")
print(convidado4 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")
print(convidado5 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")
print(convidado6 + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a "
"\nnoite; contudo, só poderei convidar duas pessoas para o evento.")

print("\n-----------------------------------------------------------------------")
print("Utilize pop() para remover os convidados de sua lista, um de cada vez até" \
"\nque apenas dois nomes permaneçam em sua lista. Sempre que remover um" \
"\nnome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela" \
"\nsaiba que você sente muito por não poder convidá-la para o jantar")

convidados = ['Marie Curie', 'D. Pedro II', 'Isaac Asimov', 'Machado de Assis', 'Teodósia', 'João Candido']

convidado1 = convidados.pop(5)
print(convidado1 + ", sentimos muito por não podermos contar com sua preseça em nosso evento.")
convidado2 = convidados.pop(4)
print(convidado2 + ", sentimos muito por não podermos contar com sua presença em nosso evento.")
convidado3 = convidados.pop(3)
print(convidado3 + ", sentimos muito por não podermos contar com sua presença em nosso evento.")
convidado4 = convidados.pop(2)
print(convidado4 + ", sentimos muito por não podermos contar com sua presença em nosso evento.")

print("\n-----------------------------------------------------------------------")
print("Apresente uma mensagem para cada uma das duas pessoas que continuam" \
"\nna lista, permitindo quelas saibam que ainda estão convidadas")

convidados = ['Marie Curie', 'D. Pedro II', 'Isaac Asimov', 'Machado de Assis', 'Teodósia', 'João Candido']

convidado5 = convidados.pop(1)
print(convidado5 + ", contamos com sua presença para o jantar.")
convidado6 = convidados.pop(0)
print(convidado6 + ", contamos com sua presença para o jantar.")

print("\n-----------------------------------------------------------------------")
print("Utilize del para remover os dois últimos nomes de sua lista, de modo que você" \
"\ntenha uma lista vazia. Mostre sua lista para garantir que você realmente tem" \
"\numa lista vazia no final de seu programa.")

del convidados[1]
print(convidados)
del convidados[0]
print(convidados)

print("\n")