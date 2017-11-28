import os

DB_PATH = 'sqlite:////home/ilopes/workspace/personal/resultados_digitais/server/database.db'
REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')