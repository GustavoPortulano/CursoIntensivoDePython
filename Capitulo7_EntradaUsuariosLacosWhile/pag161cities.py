print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\nPágina 160 - Usando a instrução break")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)  "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
