print("\n25 de julho de 2026. Sábado. Noite quente.")
print("6.1 - Pessoa: Use um dicionário para armazenar informações sobre uma pessoa" \
"\nque você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a " \
"\ncidade em que ela vive. Você deverá ter chaves como first_name, last_name," \
"\nage e city. Mostre cada informação armazenada em seu dicionário\n")

pessoa = {'first_name':'Adriano','last_name':'Silveira',
          'age':39,'city':'Belo Horizonte'}

for nome, valor in pessoa.items():
    print(f"{nome}{":"} {valor}")
    
print("\n")
    
