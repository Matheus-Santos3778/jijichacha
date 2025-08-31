import pandas as pd
import psycopg

def execute():
    with open('access/pswrd', 'r') as file:
        pswrd = file.readlines()[0].strip()

    # Conexão
    conn = psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password=pswrd
    )

    # Cursor SQL
    cur = conn.cursor()

    # Consulta
    cur.execute("SELECT * FROM tweets;")

    # Resultados
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
