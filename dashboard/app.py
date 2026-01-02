import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template
from src.db import get_connection

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM impact_summary
        ORDER BY created_at DESC
        LIMIT 1
    """)
    impact = cursor.fetchone()

    cursor.execute("""
        SELECT * FROM redistribution_results
        ORDER BY created_at DESC
        LIMIT 10
    """)
    rows = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", impact=impact, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
