from flask import Flask
from flask import request
from flask import render_template
import webbrowser
import sqlite3
import db_actions

app = Flask(__name__)

def start_server():
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(host="0.0.0.0")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_entry", methods=['post', 'get'])
def add_entry_form():
    if request.method == "POST":
        with sqlite3.connect("HTF_Hour_Database.db") as conn:
            c = conn.cursor()
        hours_worked = request.form.get("hours")
        note = request.form.get("note")
        entry = (hours_worked, note)
        db_actions.insert_work_done_today(conn, c, entry)
        # message = "Success"
        return render_template("index.html")
    else:
        return render_template("add_entry.html")

@app.route("/this_month")
def this_month():
    with sqlite3.connect("HTF_Hour_Database.db") as conn:
        c = conn.cursor()
    data = db_actions.get_data_for_this_month(c, request.args.get('m'))
    hours_worked = 0
    for rows in data:
        hours_worked += rows[4]
    return render_template("this_month.html", data=[data, hours_worked])

@app.route("/all_entries")
def all_entries():
    with sqlite3.connect("HTF_Hour_Database.db") as conn:
        c = conn.cursor()
    data = db_actions.get_all_data(c)
    hours_worked = 0
    for rows in data:
        hours_worked += rows[4]
    return render_template("all_entries.html", data=[data, hours_worked])

# if __name__ == "__main__":
#     app.run()