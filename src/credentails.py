"""
Credentials Infojobs here, replace the following line below
"""
import os
from src.utils.sanitize import credentialsFile

data = credentialsFile()

user = os.environ.get('USER') or data[0]
password = os.environ.get('PASSWORD') or data[1]

vagasUser = os.environ.get('VAGAS_USER') or data[2]
vagasPassword = os.environ.get('VAGAS_PASSWORD') or data[3]
