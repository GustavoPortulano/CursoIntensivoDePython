"""Acessando elementos de uma lista."""

print("\n")
bicycles=['trek','cannodale','redline','specialized']

print(bicycles)
print("Acessando o primeiro elemento da lista:")
print(bicycles[0])
print(bicycles[0].title())

print("Acessando o 1º e o 3º elementos da lista")
print(bicycles[0])
print(bicycles[2])

print("Acessando o último elemento da lista")
print(bicycles[-1])

print("Usando valores individuais de uma lista")
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)