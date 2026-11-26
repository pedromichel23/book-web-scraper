
import sqlite3

from .base import BooksRepository


class SQLiteBooksRepository(BooksRepository):

    def __init__(self, database="books.db"):

        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                title TEXT,
                upc TEXT,
                product_type TEXT,
                price_excl_tax REAL,
                price_incl_tax REAL,
                tax REAL,
                price REAL,
                availability INTEGER,
                num_reviews INTEGER,
                stars INTEGER,
                category TEXT,
                description TEXT
            )
        """)

        self.conn.commit()

    def save(self, item):

        description = item.get("description") or ""

        if isinstance(description, (list, tuple)):
            description = description[0] if description else ""

        self.cur.execute("""
            INSERT INTO books (
                url, title, upc, product_type,
                price_excl_tax, price_incl_tax,
                tax, price, availability,
                num_reviews, stars, category,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            item["url"],
            item["title"],
            item["upc"],
            item["product_type"],
            item["price_excl_tax"],
            item["price_incl_tax"],
            item["tax"],
            item["price"],
            item["availability"],
            item["num_reviews"],
            item["stars"],
            item["category"],
            str(description)
        ))

        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
