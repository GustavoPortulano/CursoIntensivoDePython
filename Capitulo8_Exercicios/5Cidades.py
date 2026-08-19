print("\n18 de agosto de 2026. Terça-feira. Noite fria.")
print("8.5 - Cidades: Escreva uma função chamada describe_city() que aceite o " \
"\nnome de uma cidade e seu país. A função deve exibir uma frase simples, como" \
"\nReykjavik está localizada na Islândia. Forneça um valor default ao " \
"\nparâmetro que representa o país. Chame sua função para três cidades" \
"\ndiferentes em que pelo menos uma delas não esteja no país default.")

def describe_city(cidade, pais='Brasil'):
    print("A cidade de " + cidade + " está no sul do " + pais + ".")
    
describe_city('curitiba.'.title())
describe_city('porto alegre'.title())
describe_city('punta arenas'.title(), 'chile'.title())
