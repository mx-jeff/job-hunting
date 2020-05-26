from src.utils.sanitize import sanitizeWords


def getInput():
    valores = []

    with open('../vagas.txt', 'r') as txt:
        res = txt.readlines()
        resultado = sanitizeWords(res)
        valores.append(resultado)

    print(valores)


getInput()