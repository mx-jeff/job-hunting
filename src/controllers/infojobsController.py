from src.Models.Infojobs import Infojobs


def searchInfojob():
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(str(input('[Job-hunting] Digite a vaga: ')))
        jobs.searchOptions()
        jobs.getJob()
        jobs.quitSearch()

    except Exception as error:
        jobs.quitSearch()