from time import sleep

from src.Models.vagasCom import VagasCom


def searchVagasCom():
    vagas = VagasCom()
    try:
        vagas.login()
        vagas.insertJob(str(input(f'[Job-hunting] Vaga: ')))
        vagas.searchOptions()
        vagas.selectJobs()
        vagas.subscribeJob()
        vagas.quitSearch()

    except Exception as error:
        vagas.quitSearch()
    