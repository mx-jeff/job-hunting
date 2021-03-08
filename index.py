from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
from src.controllers.apinfoController import searchApinfo
from src.utils.output import output, checkBtn
from src.config import configVar

import sys
import eel


cli = configVar['cli']
graphInferface = configVar['graphInferface']
command = configVar['command']


@eel.expose
def send(conpany, job, email_infojobs, password_infojobs, email_vagas, password_vagas):

    if conpany == "infojobs":
        searchInfojob(job, email_infojobs, password_infojobs)
        
    elif conpany == "vagas.com":
        searchVagasCom(job, email_vagas, password_vagas)
        
    else:
        output('Insira um site de vagas!')
        checkBtn()


def main():
    
    if command:
        try:
            option = sys.argv[1]
            job = str(sys.argv[2]).lower()
            str(option).lower()

            if option == "infojobs":
                searchInfojob(job, False, False)

            elif option == "vagascom":
                searchVagasCom(job, False, False)

            elif option == "apinfo":
                searchApinfo(job)

            else:
                print('Insira um site de vagas!')

        except IndexError:
            print('Insira um site de vagas!')

    if graphInferface:
        eel.init('frontend')
        eel.start('index.html', size=(600, 600))

    try:
        if cli:
            output("~" * 40)
            output(str("BUSCADOR DE EMPREGOS").center(40))
            output("~" * 40)

            option = str(input("Digite o site de busca: (infojobs ou vagas.com) ")).lower().strip()
            job = str(input('Selecione a vaga desejada: '))
            

    except IndexError:
        output('Insira um site de vagas!')
        checkBtn()

if __name__ == "__main__":
    main()
