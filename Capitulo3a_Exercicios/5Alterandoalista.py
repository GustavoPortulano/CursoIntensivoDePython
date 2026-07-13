print("\n12 de julho de 2026. Domingo, tarde fria.")
print("\n")

print("3.5 - Alterando a lista de convidados: Você acabou de saber que um de seus"
"\nconviddos não poderá comparecer ao jantar, portanto será necessário enviar"
"\num novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.")
print("\t- Comece com seu programa do Exercíco 3.4. Acrescente uma instrução print"
"\n no final de seu programa, especificando o nome do convidado que não "
"poderá comparecer.")
print("\n")
convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']
primeiraconvidada = convidados.pop()
segundoconvidado  = convidados.pop()
terceiroconvidado = convidados.pop()
print(primeiraconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(segundoconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(terceiroconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print("Alegando motivos de força maior, " + segundoconvidado + " não poderá comparecer.")
print("\n----------------------------------------------------------------------------------------------------")

print("\t- Modifique sua lista, substituindo o mone do convidado que não poderá"
"\ncomparecer pelo nome da nova pessoa que vodê está convidando.")
print("\n")
convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']
del convidados[1]
convidados.insert(1, 'Helena de Tróia')
print("Nova lista de convidados:")
print(convidados)
segundaconvidada = "Helena de Tróia"
print(primeiraconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(segundaconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(terceiroconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")

print("\n-------------------------------------------------------------------------------------------------")

print("\t- Exiba um segundo conjunto de mensagens com o convite, uma para cada"
"\npessoa que continua em sua lista.")

print("Nova lista de convidados:")
print(convidados)
segundaconvidada = "Helena de Tróia"
print(primeiraconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(segundaconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(terceiroconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")

print("\n")