import psycopg
import pandas as pd

def execute():

    with open('access/pswrd', 'r') as file:
        pswrd = file.readlines()[0].strip()

    def insert_data(data, conn_params, table_name):
        with psycopg.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                placeholders = ", ".join(["%s"] * len(data.columns))
                insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
                cur.executemany(insert_sql, data.values.tolist())
            
            conn.commit()

    conn_params = {
        "host": "localhost",
        "dbname": "postgres",
        "user": "postgres",
        "password": pswrd
    }

    data = pd.read_csv('data/tweets.csv')

    insert_data(data, conn_params, 'tweets')
    print('Dados inseridos')