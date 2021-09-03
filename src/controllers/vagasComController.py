from time import sleep

from src.Models.vagasCom import VagasCom
from src.utils.output import output, checkBtn

import eel


def searchVagasCom(targetJob, login, password):
    vagas = VagasCom()
    try:
        vagas.login(login, password)
        vagas.insertJob(targetJob)
        vagas.searchOptions()
        vagas.selectJobs()
        vagas.subscribeJob()
        vagas.quitSearch()

    except Exception as error:
        output("Algum problema ocorreu e/ou as informações estão erradas!")
        vagas.quitSearch()
        checkBtn()

    except KeyboardInterrupt:
        output('Saindo, volte sempre!')
        vagas.quitSearch()
        checkBtn()
        
