from jobhunting import Infojobs
from src.utils.output import output, checkBtn
import eel


def searchInfojob(jobTarget, login, password):
    """
    Infojobs automatic subscription job

    :jobTarget: target job to subsscribe
    :login: infojobs user to login
    :password: password to login
    """
    jobs = Infojobs(headless=True)
    site_job = jobs.appName
    job_type = jobTarget

    try:
        output(jobs, f'{site_job} Iniciando...')
        output(jobs, f'{site_job} Tentando logar...')

        if not jobs.login(login, password):
            output(jobs, f"{site_job} Login inválido ou campos errados!")
            jobs.quitSearch()
            return

        output(jobs, f'{site_job} Selecionando vaga...')
        jobs.searchList(job_type)
        output(jobs, f'{site_job} Feito!, buscando vagas para {jobTarget}')

        output(jobs, f'{site_job} Ajustando opções...')
        jobs.searchOptions()
        output(jobs, f"{site_job} Feito!")

        output(jobs, f'{site_job} Selecionando vagas disponiveis...')
        jobs.getJob()
        output(jobs, f'{site_job} {len(jobs.jobsLink)} Vagas selecionadas!')

        success = 0
        fail = 0
        output(jobs, f"{site_job} Se inscrevendo nas vagas...")

        try:
            for index, target in enumerate(jobs.jobsLink):
                if target.startswith("https://") or target.startswith("http://"):
                    status = jobs.subscribeJob(target)
                    if status == "Vaga cadastrada!":
                        success += 1

                    else:
                        fail += 1

                    output(jobs, f"{site_job} {index + 1} vaga, status: {status}")
        
        except Exception:
            output(jobs, f"{site_job} Erro ao se cadastrar, saindo...")

        jobs.quitSearch()

        output(jobs, f'{site_job} Vagas inscritas: {success}')
        output(jobs, f'{site_job} Vagas ja inscritas anteriomente ou requer preenchimento adicional: {fail}')
        output(jobs, f"{site_job} Saindo... volte sempre :)")
        checkBtn()

    except Exception as error:
        jobs.quitSearch()
        output(jobs, "Algum problema ocorreu e/ou as inforamções estão erradas!")
        output(jobs, f"Erro {error}, contate o adminstrador do sistema")
        output(jobs, f"{site_job} Saindo... volte sempre :)")
        checkBtn()

    except KeyboardInterrupt:
        output(jobs, f"{site_job} Saindo... volte sempre :)")
        jobs.quitSearch()
        checkBtn()
