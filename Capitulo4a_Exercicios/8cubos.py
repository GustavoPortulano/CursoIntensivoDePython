print("\nUm número elevado à terceira potência é chamado de cubo. por" \
"\nexemplo.o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez" \
"\nprimeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for" \
"\n para exibir o valor de cada cubo.")

cubos = []
for cubo in range(1,11):
    cubo = cubo**3
    cubos.append(cubo)
print(cubos)




