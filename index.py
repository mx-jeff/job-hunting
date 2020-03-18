from Models.Infojobs import Infojobs
import sys


def main():
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(str(input('[Job-hunting] type your prefered job: ')))
        jobs.searchOptions()
        jobs.getJob()
        #Infojobs.saveFile(Infojobs.jobsLink)
        jobs.quitSearch()

    except Exception as error:
        raise
        jobs.quitSearch()
    

if __name__ == "__main__":
    main()
