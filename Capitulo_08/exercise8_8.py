"""
8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.
"""

def make_album(name, title_album):
    album = {}
    album['Artista'] = name
    album['Título do álbum'] = title_album

    return album


albuns = []
while True:
    print(f"{'='*10}Dados do álbum{'='*10}")
    nome_artista = input("Digite o nome do artista: ")
    titulo_album = input('Informe o título do album: ')

    album = make_album(nome_artista, titulo_album)
    albuns.append(album)

    continuar = input("Você deseja incluir um novo álbum? [s/n]: ").strip().lower()[0]
    while continuar not in 'sn':
        print("Desculpe, você digitou uma informação inválida, tente novamente...")
        continuar = input("Você deseja incluir um novo álbum? [s/n]: ").strip().lower()[0]
    if continuar == 'n':
        break


print(f"{'='*10}Informações dos Álbuns{'='*10}")
for album in albuns:
    for key, value in album.items():
        print(f"{key}: {value.title()}")
    print()