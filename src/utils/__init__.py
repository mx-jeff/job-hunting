def table(href, text):
    tamanho = len(href) + 4
    print('~' * tamanho)
    print(str(text).center(tamanho))
    print()
    print(str(href))
    print('~' * tamanho)
    print()