print("\n21 de agosto de 2023. Sexta-feira. Noite agradável.")
print("\nt8.8 - Álbuns dos usuários: Comece com o seu programa do exercício 8.7." \
"\nEscreva um laço while que permita aos usuários fornecer o nome de um artista e" \
"\ncom as entradas do usuário apresente o dicionário criado. Lembre-se de incluir" \
"\num valor de saída no laço while.")

def make_album(n_artista, n_album, nr_faixas=''):
    album = {'artista':n_artista.title(), 'album':n_album.title()}
    """Condicional IF para incluir o número de faixas"""
    if nr_faixas:
         album['nr_faixas'] = nr_faixas
    else:
        """Se a condiconal não for atendica, o dicionário será mantido."""
        album
    return album

while True:
    print("Digite o nome do artista: ")
    print("Digite 'q' para sair do programa.")
    n_artista = input("Artista: ")
    if n_artista == 'q':
        break
    n_album = input("Álbum: ")
    if n_album == 'q':
        break
    n_faixas = input("Faixas: ")
    if n_faixas == 'q':
        break
    artista = make_album(n_artista.title(), n_album.title(), n_faixas)
    print(artista)
    




    