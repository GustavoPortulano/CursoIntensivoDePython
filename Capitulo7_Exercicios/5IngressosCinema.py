print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\nIngressos para o cinema: Um cinema cobra preços diferentes para os " \
"\ningressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos" \
"\nde 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o" \
"\ningresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15" \
"\ndólares. Escreva um laço em que você pergunte a idade aos usuários e, então," \
"\ninforme-lhes o preço do ingresso do cinema.")

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
 
        



