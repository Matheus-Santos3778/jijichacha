from src import insert_db, select_db, generate_data

methods = {1: generate_data.execute
            , 2: insert_db.execute
            , 3: select_db.execute}

status = True

while(status):

    status = int(input('(1) Generate Data; (2) Insert Data; (3) Show Data; (0) Exit: '))

    if status:
        methods[status]()