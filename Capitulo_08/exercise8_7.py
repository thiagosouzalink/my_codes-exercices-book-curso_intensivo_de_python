"""
8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum.
"""

def make_album(name, title_album, number_tracks=0):
    album = {}
    album['Nome'] = name
    album['Título'] = title_album
    if number_tracks:
        album['Faixas'] = number_tracks
    return album


album1 = make_album('Arctic Monkeys', 'AM')
album2 = make_album('U2', 'The Joshua Tree')
album3 = make_album('Red Hot Chili Peppers', 'Californication')
album4 = make_album('The Strokes', 'Is This It', 11)

print(album1)
print(album2)
print(album3)
print(album4)