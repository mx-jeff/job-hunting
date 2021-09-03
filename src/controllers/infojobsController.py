from src.Models.Infojobs import Infojobs
from src.utils.output import output, checkBtn
import eel


def searchInfojob(jobTarget, login, password):
    jobs = Infojobs()

    try:
        jobs.login(login, password)
        jobs.searchList(jobTarget)
        jobs.searchOptions()
        jobs.getJob()
        jobs.quitSearch()

    except Exception as error:
        output("Algum problema ocorreu e/ou as inforamções estão erradas!")
        output(f"Erro {error}, contate o adminstrador do sistema")
        checkBtn()
        jobs.quitSearch()

    except KeyboardInterrupt:
        output('Saindo, volte sempre!')
        jobs.quitSearch()
        checkBtn()
