from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB table
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL,
                       message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        message = request.form.get('message')

        if name and age and message:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, age, message) VALUES (?, ?, ?)",
                           (name, int(age), message))
            conn.commit()
            conn.close()
            return redirect('/')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, message FROM users ORDER BY id DESC LIMIT 5")
    users = cursor.fetchall()
    conn.close()

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
