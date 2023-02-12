import psycopg2 as ps
from sql_queries import create_table_queries, drop_table_queries

# remember to add logs and add it for each step.
def create_database():

    #connect to default database mahdi. 
    conn = ps.connect("host=127.0.0.1 dbname=mahdi user=postgres password=test1234")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # Create Sparkify database with UTF-8 encoding.
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    #close connection
    cur.close()

    #connect to sparkifydb 
    conn = ps.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=test1234")
    cur = conn.cursor()

    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Steps:
        1. Drops if exists and create sparkifydb
        2. Establish connection and get cursor
        3. Drop all tables
        4. Create all tables
        5. Close the connection
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur,conn)

    conn.close()

if __name__=="__main__":
    main()
