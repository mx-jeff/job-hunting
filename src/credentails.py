"""
Credentials Infojobs here, replace the following line below
"""
import os
from src.utils.words import credentialsFile

dados = credentialsFile()

user = os.environ.get('USER') or dados[0]
password = os.environ.get('PASSWORD') or dados[1]

vagasUser = os.environ.get('VAGAS_USER') or dados[2]
vagasPassword = os.environ.get('VAGAS_PASSWORD') or dados[3]
