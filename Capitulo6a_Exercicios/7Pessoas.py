print("\n30 de julho de 2026. Quinta-feira. Noite fria.")
print("5.7 - Pessoas: Comece com o exercício que você escreveu no Exercício 6.1" \
"\n(página 147). Crie dois novos dicionários que representem pessoas diferentes e" \
"\narmazene os três dicionários em uma lista chadada people. Percorra sua lista" \
"\nde pessoas com um laço. À medida que percorrer a lista, apresente tudo que " \
"\nvocê sabe sobre cada pessoa.")

adriano = {'first_name':'Adriano','last_name':'Silveira',
           'age':39,'city':'belo horizonte', }
jaqueline = {'first_name':'jaqueline','last_name':'marcy',
              'age':29,'city':'esmeraldas', }
vilma = {'first_name':'vilma','last_name':'pedralissa',
         'age':39,'city':'petropolis', }

"""Lista de dicionários"""
people = [adriano, jaqueline, vilma]

print("\n")

for pessoa in people:
    full_name =     f"{pessoa['first_name']} {pessoa['last_name']}"
    persons_age =   f"{pessoa['age']}"
    city =          f"{pessoa['city']}"
    print(f"Nome: {full_name.title()}")
    print(f"Idade: {persons_age} anos")
    print(f"Cidade: {city.title()}")
    print("\n")

