from rq import Worker, Queue, Connection
import redis

listen = ['default']
redis_url = redis.Redis(host='localhost', port=6379)

if __name__ == '__main__':
    with Connection(redis_url):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
