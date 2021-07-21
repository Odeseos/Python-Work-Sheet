import datetime

def insert_work_done_today(conn, c, entry):
    current_year = "{0.year}".format(datetime.datetime.now())
    current_month = "{0.month}".format(datetime.datetime.now())
    current_day = "{0.day}".format(datetime.datetime.now())
    sql_code = f"""
        INSERT INTO time_sheet(year, month, day, hours_worked, notes)
        VALUES({current_year}, {current_month}, {current_day}, ?, ?);
    """
    try:
        c.execute(sql_code, entry)
        conn.commit()
        print("SUCCESS: Query has been added to the database!")
    except Exception as e:
        print(e)

def get_all_data(c):
    sql_code = """
        SELECT * FROM time_sheet;
    """
    c.execute(sql_code)
    data = c.fetchall()
    return data

    # print(f"I've worked a total of \\- {str(total_time_worked)} -/ hours.")

def get_data_for_this_month(c, month):
    sql_code = f"""
            SELECT * FROM time_sheet WHERE month = {month};
        """
    c.execute(sql_code)
    data = c.fetchall()
    return data