print("\n21 de agosto de 2026. Sexta-feira. Noite agradável.")
print("\n\t8.7 - Álbum: Escreva uma função chamada make_album que construa um " \
"\ndicionário descrevendo um álbum musical. A função deve aceitar o nome de um" \
"\nartista e o título de um álbum e deve devolver um dicionário contendo essas" \
"\nduas informações. Use a função para criar três dicionários que representem " \
"\nálbuns diferentes. Apresente cada valor devolvido para mostrar que os" \
"\ndicionários estão armazenando as informações do álbum corretamente." \
"\n\tAcrescente um parâmetro opcionam em make_album() que permita armazenar" \
"\no número de faixas em um álbum. Se a linha que fizer a chamdada incluir um" \
"\nvalor para o número de faixas, acrescente esse valor ao diconário do álbum." \
"\nFaça o menos uma nova chamada da função incluindo o número de faixas " \
"\nem um álbum.\n")

def make_album(n_artista, n_album, nr_faixas=''):
    album = {'artista':n_artista.title(), 'album':n_album.title()}
    """Condicional IF para incluir o número de faixas"""
    if nr_faixas:
        album['nr_faixas'] = nr_faixas
    else:
        """Se a condiconal não for atendica, o dicionário será mantido."""
        album
    return album

artista = make_album('titans', 'cabeça de dinossauro', nr_faixas=11)
print(artista)
artista = make_album('legião urbana', 'dois')
print(artista)
artista = make_album('vangelis','blade runner')
print(artista)

print("\n")


