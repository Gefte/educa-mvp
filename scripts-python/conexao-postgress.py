import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd

load_dotenv('scripts-python/.env')



db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

try:
    connection = psycopg2.connect(**db_params)
    print("Conexão ao banco de dados bem-sucedida!")

    

except Exception as e:
    print("Erro:", e)
finally:
    if connection:
        connection.close()
        print("Conexão encerrada.")
