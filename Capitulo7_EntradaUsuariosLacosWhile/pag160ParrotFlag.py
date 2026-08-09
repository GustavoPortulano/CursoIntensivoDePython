print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\nPágina 159 - Usando uma flag")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

"""Uso de uma flag:"""
active = True

while active: 
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print("\n")