meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "Abreviação da palavra 'verdade'",
            "FARMAR": "Obter algo de maneira eficiente e rapido",
            }
palavras = input("escreva uma palavra da atualidade que não sabe o significado. (ESCREVA EM LETRA MAIUSCULAS)")

if palavras in meme_dict.keys():
    print(meme_dict[palavras])
    # O que devemos fazer se a palavra for encontrada?
else:

    print('Não possuimos essa palavra no sistema')
    # O que devemos fazer se a palavra não for encontrada?
