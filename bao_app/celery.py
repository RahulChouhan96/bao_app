# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bao_app.settings')

# create a Celery instance and configure it.
app = Celery('bao_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Periodic task
app.conf.beat_schedule = {
    'fetch-and-cache-films-data': {
        'task': 'myapp.tasks.fetch_and_cache_films_data',
        'schedule': 60.0,  # Run every 60 seconds (1 minute)
    },
}
