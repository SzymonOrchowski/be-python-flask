import psycopg2
from config import config

def createTable():
    queries = (
        """
        DROP TABLE IF EXISTS recipes;
        """,
        """
        CREATE TABLE recipes (
            id SERIAL UNIQUE PRIMARY KEY,
            original_id VARCHAR(15),
            imageUrl VARCHAR(255),
            instructions TEXT,
            ingredients TEXT
        );
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for query in queries:
            cur.execute(query)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insertData():
    print('insertData')

if __name__ == "__main__":
    createTable()
    insertData()