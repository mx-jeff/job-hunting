from time import sleep

from src.Models.vagasCom import VagasCom


def searchVagasCom():
    vagas = VagasCom()
    try:
        vagas.login()
        vagas.insertJob()
        vagas.searchOptions()
    
    except Exception as error:
        raise
        vagas.quitSearch()
    