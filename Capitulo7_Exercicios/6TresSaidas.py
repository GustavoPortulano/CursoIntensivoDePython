print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\nEscreva versões diferentes do Exercício 7.4 ou 7.5 que faça o swguite:" \
"\n\tUse um teste condicional na instrução while para encerrar o laço;" \
"\n\tuse uma variável active para controlar o tempo que o laço executará;" \
"\n\tuse uma instrução break para sair do laço quando o usuário fornecer o valor quit.")

print("\n")

print("\n")

prompt = "Qual a sua idade? "
prompt_saida = "Para sair do programa, digite 'quit'." \
                "\nPara prosseguir, pressione a tecla 'ENTER.'"

saida_programa = True

while saida_programa:
    mensagem = int(input(prompt))
    if mensagem <= 3:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso é gratuito.")
    elif 3 < mensagem <= 12:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso custa 10 dólares")
    elif mensagem >= 12:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso custa 15 dólares.")
    mensagem_saida = str(input(prompt_saida))
    if mensagem_saida == 'quit':
        saida_programa = False
print("\n")

print("\nUsando uma instrução break.")
prompt = "Qual a sua idade? "

while True:
    mensagem = int(input(prompt))
    if mensagem <= 3:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso é gratuito.")
    elif 3 < mensagem <= 12:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso custa 10 dólares")
    elif mensagem >= 12:
        print(f"Sua idade é de {mensagem} anos. Seu ingresso custa 15 dólares.")
    break
    
print("\n")