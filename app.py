
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "app-password"),
        database=os.getenv("DB_NAME", "notes_db")
    )

def initialize_db():
    for attempt in range(15):
        try:
            connection = get_db()
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    content VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()
            cursor.close()
            connection.close()
            return
        except mysql.connector.Error:
            if attempt == 14:
                raise
            time.sleep(2)

@app.route("/", methods=["GET", "POST"])
def home():
    connection = get_db()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        content = request.form.get("content", "").strip()
        if content:
            cursor.execute(
                "INSERT INTO notes (content) VALUES (%s)",
                (content,)
            )
            connection.commit()

        cursor.close()
        connection.close()
        return redirect(url_for("home"))

    cursor.execute("SELECT id, content FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", notes=notes)

initialize_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
