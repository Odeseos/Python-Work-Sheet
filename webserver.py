from flask import Flask, request, render_template
import datetime
import webbrowser
import sqlite3
import db_actions

app = Flask(__name__)

def start_server():
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(host='0.0.0.0')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_entry', methods=['get', 'post'])
def add_entry_form():
    if request.method == 'POST':
        with sqlite3.connect('HTF_Hour_Database.db') as conn:
            c = conn.cursor()
        hours_worked = request.form.get('hours')
        note = request.form.get('note')
        entry = (hours_worked, note)
        db_actions.insert_work_done_today(conn, c, entry)
        # message = 'Success'
        return render_template('index.html')
    if request.method == 'GET':
        return render_template('add_entry.html')

@app.route('/get_month/<month>')
def get_month(month):
    with sqlite3.connect('HTF_Hour_Database.db') as conn:
        c = conn.cursor()
    if month == "all":
        data = db_actions.get_all_data(c)
        month_name = "everything"
        title = "All Entries"
    elif int(month) >= 1 and int(month) <= 12:
        data = db_actions.get_data_for_this_month(c, month)
        month_name = datetime.datetime.strptime(month, '%m').strftime('%B')
        title = "Entries from " + month_name
    hours_worked = 0
    for rows in data:
        hours_worked += rows[4]
    return render_template('get_month.html', data=[data, hours_worked, month_name, title])

# if __name__ == '__main__':
#     app.run()