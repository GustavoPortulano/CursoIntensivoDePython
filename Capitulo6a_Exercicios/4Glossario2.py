print("\n28 de julho de 2026. Terça-feira. Noite fria.")
print("6.4 - Glossário2: Agora qeu você já sabe como percorrer um dicionário com" \
"\num laço, limpe o código do Exercício 6.3 (página 148), substituindo sua" \
"\nsequência de instruções print por um laço que percorra as chaves e os valores" \
"\ndo dicionário. Quando tiver certeza de que seu laço funciona.acrescente mais" \
"\ncinco termos Python ao seu glossário. Ao executar seu programa novamente," \
"\nessas palavras e significados novos deverão ser automaticamente incluídos na" \
"\nsaída.")

glossario = {'FALSE':'Representa um valor booleano de falso. Essa palavra é usada '
            'para indicar que uma condição não é verdadeira',
            'TRUE':'O oposto de False, essa palavra representa um valor booleano '
            'verdadeiro. É usada para indicar que uma condição é verdadeira no código.',
            'IF':'Ela inicia uma instrução condicional que executará um bloco '
            'de código se uma determinada condição for verdadeira.',
            'OR':'Esse operador também é utilizado para analisar mais de uma condição, '
            'porém ele retorna verdadeiro se pelo menos uma das expressões for verdadeira.',
            'ELAW':'O else também faz parte das estruturas condicionais do Python. '
            'Essa palavra define um bloco de código que deve ser executado se todas as '
            'condições anteriores não forem verdadeiras.',
            'ELIF':'Abreviação de “else if”, essa palavra é usada após uma instrução if'
            ' para verificar outra condição caso a primeira não seja verdadeira.',
            'IS':'A palavra is é um operador de comparação em Python que verifica '
            'se duas variáveis referenciam o mesmo objeto na memória.',
            'IN':'O in é um operador de comparação que verifica se um item está presente'
            'em uma sequência, como uma lista ou uma string, como visto no exemplo da palavra not.'}

for palavra in glossario.items():
    print(palavra)
    print("\n")
    