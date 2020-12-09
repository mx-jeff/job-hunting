from time import sleep

from src.Models.vagasCom import VagasCom
from src.utils.output import output

import eel


def searchVagasCom(targetJob):
    vagas = VagasCom()
    try:
        vagas.login()
        vagas.insertJob(targetJob)
        vagas.searchOptions()
        vagas.selectJobs()
        vagas.subscribeJob()
        vagas.quitSearch()

    except Exception as error:
        output("Algum problema ocorreu e/ou as inforamções estão erradas!")
        vagas.quitSearch()
        eel.enableButton()
