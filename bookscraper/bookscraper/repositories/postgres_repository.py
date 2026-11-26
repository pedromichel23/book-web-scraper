#import psycopg
from .base import BooksRepository

class PostgreSQLBooksRepository(BooksRepository):

    def __init__(self, host, user, password, database):
        # Create PostgreSQL connection
        pass

    def save(self, item):
        # Insert book into PostgreSQL
        pass

    def close(self):
        # Close connection
        pass