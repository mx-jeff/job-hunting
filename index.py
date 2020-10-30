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
    

    # try:
    #     print("~" * 40)
    #     print(str("BUSCADOR DE EMPREGOS").center(40))
    #     print("~" * 40)

    #     option = str(input("Digite o site de busca: (infojobs ou vagas.com) ")).lower().strip()
    #     job = str(input('Selecione a vaga desejada: '))

    #     if option == "infojobs":
    #         searchInfojob(job)

    #     elif option == "vagas.com":
    #         searchVagasCom(job)
        
    #     else:
    #         print('Insira um site de vagas!')

    # except IndexError:
    #     print('Insira um site de vagas!')


if __name__ == "__main__":
    main()
