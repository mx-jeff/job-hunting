from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
from src.controllers.apinfoController import searchApinfo
from src.utils.output import output
import sys
import eel


def main():
    
    # try:
    #     option = sys.argv[1]
    #     job = str(sys.argv[2]).lower()
    #     str(option).lower()

    #     if option == "infojobs":
    #         searchInfojob(job)

    #     elif option == "vagascom":
    #         searchVagasCom(job)

    #     elif option == "apinfo":
    #         searchApinfo(job)

    #     else:
    #         print('Insira um site de vagas!')

    # except IndexError:
    #     print('Insira um site de vagas!')

    eel.init('frontend')

    try:
        output("~" * 40)
        output(str("BUSCADOR DE EMPREGOS").center(40))
        output("~" * 40)

        option = str(input("Digite o site de busca: (infojobs ou vagas.com) ")).lower().strip()
        job = str(input('Selecione a vaga desejada: '))

        eel.start('index.html', size=(600, 300))

        if option == "infojobs":
            searchInfojob(job)

        elif option == "vagas.com":
            searchVagasCom(job)
        
        else:
            output('Insira um site de vagas!')

    except IndexError:
        output('Insira um site de vagas!')

if __name__ == "__main__":
    main()
