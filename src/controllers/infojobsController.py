from jobhunting import Infojobs
from src.utils.output import output, checkBtn
import eel
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def searchInfojob(jobTarget, login, password):
    """
    Infojobs automatic subscription job

    :jobTarget: target job to subsscribe
    :login: infojobs user to login
    :password: password to login
    """
    jobs = Infojobs(headless=False)
    site_job = jobs.appName
    job_type = jobTarget

    try:
        output(f'{site_job} Iniciando...')
        output(f'{site_job} Tentando logar...')

        if not jobs.login(login, password):
            output(f"{site_job} Login inválido ou campos errados!")
            jobs.quitSearch()
            return

        output(f'{site_job} Selecionando vaga...')
        jobs.searchList(job_type)
        output(f'{site_job} Feito!, buscando vagas para {jobTarget}')

        # output(f'{site_job} Ajustando opções...')
        # jobs.searchOptions()
        # output(f"{site_job} Feito!")

        output(f'{site_job} Selecionando vagas disponiveis...')
        jobs.getJob()
        output(f'{site_job} {len(jobs.jobsLink)} Vagas selecionadas!')

        success = 0
        fail = 0
        output(f"{site_job} Se inscrevendo nas vagas...")

 
        try:
            for index, target in enumerate(jobs.jobsLink):
                if target.startswith("https://") or target.startswith("http://"):
                    status = jobs.subscribeJob(target)
                    if status == "Vaga cadastrada!":
                        success += 1

                    else:
                        fail += 1

                    output(f"{site_job} vaga {index + 1}/{len(jobs.jobsLink)}, status: {status}", True)
            
            print('........')
        
        except Exception:
            output(f"{site_job} Erro ao se cadastrar, saindo...")

        jobs.quitSearch()

        output(f'{site_job} Vagas inscritas: {success} \n')
        output(f'{site_job} Vagas ja inscritas anteriomente ou requer preenchimento adicional: {fail}')
        output(f"{site_job} Saindo... volte sempre :)")
        checkBtn()

    except Exception as error:
        jobs.quitSearch()
        output("Algum problema ocorreu e/ou as inforamções estão erradas!")
        output(f"Erro {error}, contate o adminstrador do sistema")
        output(f"{site_job} Saindo... volte sempre :)")
        checkBtn()
        raise

    except KeyboardInterrupt:
        output(f"{site_job} Saindo... volte sempre :)")
        jobs.quitSearch()
        checkBtn()
