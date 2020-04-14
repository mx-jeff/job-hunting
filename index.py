from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
import sys


def main():
    option = sys.argv[1]
    str(option).lower()

    try:
        if option == "infojobs":
            searchInfojob()

        elif option == "vagascom":
            searchVagasCom()
        
        else:
            print('Insira um site de vagas!')

    except IndexError:
        print('Insira um site de vagas!')

if __name__ == "__main__":
    main()
