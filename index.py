from Models.Infojobs import Infojobs
import sys


def main():
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(str(input("Digite sua vaga: ")))
        jobs.searchOptions()
        jobs.getJob()
        #Infojobs.saveFile(Infojobs.jobsLink)
        jobs.quitSearch()

    except Exception as error:
        jobs.quitSearch()
    

if __name__ == "__main__":
    main()
