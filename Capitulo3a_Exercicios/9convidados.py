print("\n13 de julho de 2026. Segunda-feria. Noite fria.")
print("3.9 - Convidados para o jantar: Trabalhando com um dos programas dos " \
"\nexercícios de 3.4 a 3.7, use len() para exibir uma" \
"\nmensagem informando o número de pessoa que você está convidando" \
"\npara o jantar.")

"""Obs: Para concatenar string e número foi usado print(f"... {len()}...)"""

convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']

print(len(convidados))

primeiraconvidada = convidados.pop()
segundoconvidado  = convidados.pop()
terceiroconvidado = convidados.pop()
print(primeiraconvidada + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(segundoconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")
print(terceiroconvidado + " , boa noite, gostaria que comparecesse à um jantar em minha casa hoje a noite.")

convidados = ['D. Pedro II', 'Machado de Assis', 'Teodósia']
print(f"O jantar contará com {len(convidados)} participantes")
print("\n")



