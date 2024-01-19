from flask import Flask,request,render_template
app = Flask(__name__)
import sqlite3


def get_contacts():
    with sqlite3.connect('contacts.db') as conn:
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM contacts")
        return rows.fetchall()
    






@app.route('/')
def home():
    return render_template('home.html',contacts=get_contacts())


