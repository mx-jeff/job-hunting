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
        
        print("Algum problema ocorreu e/ou as inforamções estão erradas!")
        jobs.quitSearch()