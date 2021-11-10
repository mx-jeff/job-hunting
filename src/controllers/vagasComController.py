from time import sleep

from jobhunting import VagasCom
from src.utils.output import output, checkBtn

import eel


def searchVagasCom(targetJob, login, password):
    vagas = VagasCom(headless=True)
    job_site = vagas.appName

    output(f'{job_site} Iniciando...')
    try:
        output(f'{job_site} Tentando logar...')
        if not vagas.login(login, password):
            vagas.quitSearch()
            output(f'{job_site} Login inválido ou campos errados!')
            output("[Vagas.com] Saindo... volte sempre :)")
            return 

        output(f'{job_site} logado com sucesso!')

        output(f'{job_site} A selecionar vaga...')
        vagas.insertJob(targetJob)
        output(f'{job_site} Vaga selecionada!')

        output(f'{job_site} A ajustar opções...')
        vagas.searchOptions()
        output(f'{job_site} Feito!')

        output(f'{job_site} Listando Vagas...')
        vagas.selectJobs()
        output(f'{job_site} Feito!')
        output(f"{len(vagas.targetLink)} vagas encontradas!")

        success = 0
        fail = 0
        output(f"{job_site} Se inscrevendo nas vagas...")

        try:
            for index, target in enumerate(vagas.targetLink):
                if target.startswith("https://") or target.startswith("http://"):
                    status = vagas.subscribeJob(target)
                    if status == "Vaga cadastrada!":
                        success += 1

                    else:
                        fail += 1

                    output(f"{job_site} {index + 1} vaga, status: {status}")

        except Exception:  
            output(f"{job_site} erro ao se inscrever!")

        finally:
            vagas.quitSearch()

        output(f'{job_site} Vagas inscritas: {success}')
        output(f'{job_site} Vagas ja inscritas anteriomente ou requer preenchimento adicional: {fail}')
        output(f"{job_site} Saindo... volte sempre :)")
        checkBtn()

    except Exception as error:
        vagas.quitSearch()
        output("Algum problema ocorreu e/ou as informações estão erradas!")
        output(f"{job_site} Saindo... volte sempre :)")
        checkBtn()

    except KeyboardInterrupt:
        vagas.quitSearch()
        output(f"{job_site} Saindo... volte sempre :)")
        checkBtn()
        
