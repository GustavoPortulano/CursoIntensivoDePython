print("\n22 de agosto de 2026. Sábado. Noite fria.")
print("Página 182 - Passando uma lista para uma função.")

def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    """A lista é representada pelo parâmetro names."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

"""Passando valores para a lista fora do laço for:"""
usernames = ['hannah','ty','margot']
"""Chamada da função fora do laço for:"""
greet_users(usernames)

