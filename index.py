from Models.Infojobs import Infojobs
import sys


def main():
    jobs = Infojobs()

    try:
        jobs.login()
        jobs.searchList(sys.argv[1])
        jobs.searchOptions()
        jobs.getJob()
        #Infojobs.saveFile(Infojobs.jobsLink)
        jobs.quitSearch()

    except Exception as error:
        print(error)
        jobs.quitSearch()
    

if __name__ == "__main__":
    main()
