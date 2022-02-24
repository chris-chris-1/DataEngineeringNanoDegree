import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Creates and connects to the sparkify database. Returns the connection and cursor to the sparkify database.

    Arguments:
        None
        
    :return:
        conn (connection): A instance of the connection class
        cur (cursor): A client side cursor object (to execute SQL queries)
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    # conn.close()
    # create sparkify database with UTF8 encoding
    # cur.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'my_DB';")
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    # conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.

    Arguments:
        :param cur: A client side cursor object
        :param conn: A instance of the connection class

    :return:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.

    Arguments:
        :param cur: A client side cursor object
        :param conn: A instance of the connection class

    :return:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Drops (if exists) and creates the sparkify database.
    Establishes connection with the sparkify database and gets cursor to it.
    Drops all the tables.
    Creates all tables needed.
    Closes the connection.

    Arguments:
        None

    :return:
        None
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()