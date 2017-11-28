import redis

import config

redis_conn = redis.from_url(config.REDIS_URL)