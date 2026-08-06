print("\n30 de julho de 2026. Quinta-feira. Noite fria.")
print("6.11 - Cidades: Crie um dicionário chamado cities. Use os nomes de três" \
"\ncidades como chaves em seu dicionário. Crie um dicionário com informações" \
"sobre cada cidade e inclua o país em que a cidade está localizada, a população" \
"\naproxixmada e um fato sobre essa cidade. As chaves do dicionário de cada cidade" \
"\ne todas as informações como country, population e fact. Apresente o nome de cada" \
"\ncidade e toas as informações que você armazenou sobre ela.")

print("\n")

cities = {'isntabul':{'country':'turquia',
            'population':'5 milhões',
            'fact':'antiga capital bizantina e otomana'},
          'rio de janeiro':{'country':'brasil',
            'population':'5 milhões e 500 mil',
            'fact':'antiga capital imperial do Brasil'},
          'jerusalem':{'country':'israel',
            'population':'2 milhões e 300 mil de habitantes',
            'fact':'cidade disputada por três religiões'}}

for cidade, fatos in cities.items():
    country     = fatos['country']
    population  = fatos['population']
    fact        = fatos['fact']
    print(cidade.title())
    print(f"País: {country.title() + ";"}"      + 
          f"\nPopulação: {population}" + ";"    +
          f"\nFato: {fact}." + "\n.............")
   

    