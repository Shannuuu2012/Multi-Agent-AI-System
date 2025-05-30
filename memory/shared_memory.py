import redis
import json
from datetime import datetime

# Connect to Redis server (make sure Redis is running)
r = redis.Redis(host='localhost', port=6379, db=0)

def save_to_memory(data):
    data['timestamp'] = datetime.utcnow().isoformat()
    r.rpush('memory_store', json.dumps(data))

def get_memory():
    entries = r.lrange('memory_store', 0, -1)
    return [json.loads(entry) for entry in entries]
