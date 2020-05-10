from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
import sys


def main():
    try:
        option = sys.argv[1]
        job = str(sys.argv[2]).lower()
        str(option).lower()

        if option == "infojobs":
            searchInfojob(job)

        elif option == "vagascom":
            searchVagasCom(job)
        
        else:
            print('Insira um site de vagas!')

    except IndexError:
        print('Insira um site de vagas!')

if __name__ == "__main__":
    main()
