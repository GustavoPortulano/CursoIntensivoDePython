print("\n09 de agosto de 2026. Domingo. Tarde normal.")
print("\nPágina 165 - Removendo todas as instâncias de valores específicos de uma lista.")

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)