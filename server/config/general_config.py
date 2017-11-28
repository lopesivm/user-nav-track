import os

DB_PATH = 'sqlite:////tmp/database.db'
REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
