def table(href, text):
    tamanho = len(href) + 4
    print('~' * tamanho)
    print(str(text).center(tamanho))
    print()
    print(str(href))
    print('~' * tamanho)
    print()

def timer():
    from time import sleep

    sleep(5)

def alert(browser):
    alert = browser.switch_to.alert
    alert.accept()