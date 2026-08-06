print("\n06 de agosto de 2026. Quinta-feira. Inicio de madrugada.")
print("CAPITULO 7 - ENTRADA DE USUÁRIO E LAÇOS WHILE")

"""Mensagem inicial do programa;"""
"""Digitar quit para finalizar o programa;"""
"""Armazena o valor da mensagem;"""
"""Message vazia: usada no inicio do laço para a primeira comparação."""
"""Instrução IF: evita a repetição de 'quit' no final do programa."""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = " "

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)