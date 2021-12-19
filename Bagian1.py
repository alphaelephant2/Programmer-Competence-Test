import psycopg2
from psycopg2 import Error

# Connect to an existing database
try: 
    conn = psycopg2.connect(user="postgres",
                            password="postgre",
                            host="127.0.0.1",
                            port="5432",
                            database="LSP")

    # Create a cursor to perform database operations
    cursor = conn.cursor()
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    # Text to integer converter function
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
        sql = """UPDATE bagian1 set angka = %s where id = %s"""
        
        for key, value in help_dict.items():
            if kata_angka == key:
                cursor.execute(sql, (value, kata_id))
                # conn.commit()

    # Get query result
    cursor.execute("""SELECT * from bagian1""")

    # Fetches rows of a query result and return a list of tuples
    for row in cursor.fetchall():
        text2int(row)

    # Convert column angka's data type from varchar to integer
    cursor.execute("""ALTER TABLE bagian1 ALTER COLUMN angka TYPE integer USING (angka::integer)""")
    
    # Sort column angka
    sort = """SELECT * from bagian1 ORDER BY angka"""
    cursor.execute(sort)
    sorted = cursor.fetchall()
    # conn.commit()

    # Identify column angka as odd/even and delete all odd numbers
    print('Sorting secara ascending dan penentuan ganjil/genap')
    for row in sorted:
        if row[1] % 2 != 0:
            num = 'ganjil'
            cursor.execute("""DELETE from bagian1 where id = %s""", [row[0]])
        else:
            num = 'genap'
        print('id: ', row[0])
        print('angka: ', row[1])
        print('jenis: ', num)
        # conn.commit()
    print('\n')
    
    # Print after odd numbers deleted
    print('Setelah penghapusan bilangan ganjil')
    cursor.execute(sort)
    for row in cursor.fetchall():
        print('id: ', row[0])
        print('angka: ', row[1])
        

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")