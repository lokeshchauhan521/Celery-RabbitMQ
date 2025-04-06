# from .celery_worker import app  
# @app.task
# def add(x, y):
#     return x + y

# app/tasks.py
from celery import shared_task

@shared_task
def add(x , y):
    return x + y

@shared_task
def multi(x,y):
    return x * y