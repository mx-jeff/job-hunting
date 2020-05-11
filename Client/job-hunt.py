from os import system 

jobsSite = ["infojobs", "vagascom"]
jobs = ["python","php","javascript","front-end","home office ti"]


for jobSite in jobsSite:
    for job in jobs:
        system(f"heroku run -a jober-hunt python index.py {jobSite} {job}")
