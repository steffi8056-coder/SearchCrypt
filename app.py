from flask import Flask, render_template, request, redirect
import sqlite3
from encryption import encrypt_data,decrypt_data

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    name = request.form["name"]
    department = request.form["department"]


    encrypted_name=encrypt_data(name)
    encrypted_department=encrypt_data(department)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (name, department) VALUES (?, ?)",
        (encrypted_name,encrypted_department)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    create_database()
    app.run(debug=True)



    