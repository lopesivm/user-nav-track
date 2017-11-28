from rq import Worker, Queue, Connection

import config
from models import init_engine
from workers import redis_conn

listen = ['default']

init_engine(config.DB_PATH, pool_recycle=1)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()