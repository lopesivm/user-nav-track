import os

DB_PATH = os.getenv('JAWSDB_URL', 'sqlite:////tmp/database.db')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
