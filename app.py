from flask import Flask
import sqlite3

app = Flask(__name__)

# 🔸 Funkcja pomocnicza do pobierania zawodników z bazy
def get_zawodnicy():
    # połączenie z bazą
    conn = sqlite3.connect("data/karate.db")
    cursor = conn.cursor()

    # wykonanie zapytania
    cursor.execute("SELECT id, imie, nazwisko, waga, klub FROM Zawodnicy")
    rows = cursor.fetchall()  # lista krotek

    conn.close()
    return rows

# 🔸 Strona główna - test
@app.route("/")
def home():
    zawodnicy = get_zawodnicy()

    # Proste sformatowanie wyniku w HTML
    html = "<h1>Lista zawodników</h1><table border='1' cellpadding='5'>"
    html += "<tr><th>ID</th><th>Imię</th><th>Nazwisko</th><th>Waga</th><th>Klub</th></tr>"

    for z in zawodnicy:
        html += f"<tr><td>{z[0]}</td><td>{z[1]}</td><td>{z[2]}</td><td>{z[3]}</td><td>{z[4]}</td></tr>"

    html += "</table>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
