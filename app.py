import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return '<body style="background-color: lightblue;"><h1>Hello, Render with Docker!</h1></body>'.format(count)

@app.route('/about')
def about():
    return '<h1>PRUEBAS</h1>'