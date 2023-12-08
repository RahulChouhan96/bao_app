# myapp/tasks.py
from celery import shared_task
from django.core.management import call_command

@shared_task
def fetch_and_cache_external_data():
    call_command('get_all_films')
