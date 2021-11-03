
from __future__ import absolute_import, unicode_literals

from celery import Celery
from .views import GetRate

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def post(x,y):
    #fetching the api
    a = GetRate()
    a.post()
    