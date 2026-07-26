print("\n26 de julho de 2026. Domingo. Madrugada fria.")
print("6.3 - Glossário: Um dicionário Python pode ser usado para modelar" \
"\num dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo" \
"\nde glossário." \
"\n\t * Pense em cinco palavras relacionadas à programação que você conheceu" \
"\nnos capítulos anteriores. Use essas palavres como chaves em seu glossário e" \
"\narmazene seus significados como valores." \
"\n\tMostre cada palavra e seu significado em uma saída formatada de modo" \
"elegante.")

#É possível usar quebra de linha dentro do dicionário para impressão.

glossario = {'False':'Representa um valor booleano de falso. Essa palavra é usada '
            '\npara indicar que uma condição não é verdadeira',
            'True':'O oposto de False, essa palavra representa um valor booleano '
            '\nverdadeiro. É usada para indicar que uma condição é verdadeira no código.',
            'If':'Ela inicia uma instrução condicional que executará um bloco '
            '\nde código se uma determinada condição for verdadeira.',}

for palavra in glossario:
    print("\n" + palavra + f": {glossario[palavra]}")

print("\n")