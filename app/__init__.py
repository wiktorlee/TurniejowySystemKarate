from flask import Flask, g
from sqlalchemy import create_engine, text
import os

def get_engine():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("Brak zmiennej środowiskowej DATABASE_URL")
    # Supabase zwykle wymaga SSL:
    if "?sslmode=" not in url:
        url += "?sslmode=require"
    return create_engine(f"postgresql+psycopg://{url.split('://', 1)[1]}", pool_pre_ping=True, future=True)


def get_db():
    if "db" not in g:
        g.db = get_engine().connect()
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def create_app():
    app = Flask(__name__)
    app.teardown_appcontext(close_db)

    @app.cli.command("init-db")
    def init_db():
        db = get_db()
        with open("app/models/schema.pg.sql", "r", encoding="utf-8") as f:
            db.execute(text(f.read()))
        db.commit()
        print("✅ Postgres schema loaded (Supabase)")

    @app.cli.command("seed")
    def seed():
        db = get_db()
        with open("app/models/seed.pg.sql", "r", encoding="utf-8") as f:
            db.execute(text(f.read()))
        db.commit()
        print("🌱 Seed data inserted (Supabase)")

    @app.route("/")
    def home():
        return "Supabase działa!"

    return app
