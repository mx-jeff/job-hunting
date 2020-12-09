from src.Models.Infojobs import Infojobs
from src.utils.output import output
import eel

def searchInfojob(jobTarget):
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(jobTarget)
        jobs.searchOptions()
        jobs.getJob()
        jobs.quitSearch()

    except Exception as error:
        output("Algum problema ocorreu e/ou as inforamções estão erradas!")
        eel.enableButton()
        jobs.quitSearch()