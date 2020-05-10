from src.Models.Infojobs import Infojobs


def searchInfojob(jobTarget):
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(jobTarget)
        jobs.searchOptions()
        jobs.getJob()
        jobs.quitSearch()

    except Exception as error:
        jobs.quitSearch()