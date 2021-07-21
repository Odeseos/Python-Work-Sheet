import sqlite3
import webserver

# Create time sheet table if not present
def create_table(conn):
    sql_code = """
        CREATE TABLE IF NOT EXISTS time_sheet(
            id integer PRIMARY KEY,
            year int NOT NULL,
            month int NOT NULL,
            day int NOT NULL,
            hours_worked integer,
            notes longtext
        );
    """
    try:
        c = conn.cursor()
        c.execute(sql_code)
    except Exception as e:
        print(e)

def main():
    # Creates connection to database since
    # you can't connect to the db on a different core
    with sqlite3.connect("HTF_Hour_Database.db") as conn:
        create_table(conn)
    webserver.start_server()

if __name__ == '__main__':
    main()