"""
To start workers
----------------------------------------------------------------
celery -A add_task[module_name] worker --loglevel=INFO

"""

from celery import Celery

app = Celery('addTask', backend='rpc://', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
