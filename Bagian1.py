import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="postgre",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="LSP")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    def text2int(kata):
        help_dict = {
            'satu': 1,
            'dua': 2,
            'tiga': 3,
            'empat': 4,
            'lima': 5,
            'enam': 6,
            'tujuh': 7,
            'delapan': 8,
            'sembilan': 9,
            'sepuluh' : 10
        }

        kata_id = kata[0]
        kata_angka = kata[1]
        sql = """ UPDATE bagian1 set angka = %s where id = %s"""
    
        for key, value in help_dict.items():
            if kata_angka == key:
                cursor.execute(sql, (value, kata_id))
                connection.commit()


    getAll = "select * from bagian1"
    cursor.execute(getAll)
    
    records = cursor.fetchall()
    for row in records:
        text2int(row)

    cursor.execute("ALTER TABLE bagian1 ALTER COLUMN angka TYPE integer USING (angka::integer)")
    
    cursor.execute("SELECT * from bagian1 ORDER BY angka")
    print(cursor.fetchall())
    connection.commit()

    columns = []
    rows = cursor.execute('select * from bagian1')
    for row in rows:
        columns.append(row['angka'])
    print(columns)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

