from celery import Celery, result

celery = Celery('tasks', broker='amqp://guest:guest@10.0.7.10:5672//', backend='rpc://')
celery.conf.task_default_queue = 'default'

@celery.task
def post_request(value):
    return value

@celery.task
def get_response(id):
    response = result.AsyncResult(id)
    return response.status

