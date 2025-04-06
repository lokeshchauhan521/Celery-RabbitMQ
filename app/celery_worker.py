from celery import Celery

app = Celery(
    "my_app",
    broker="pyamqp://guest@localhost//",
    backend="rpc://"
)

app.autodiscover_tasks(['app.tasks'])
