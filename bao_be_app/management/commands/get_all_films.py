# myapp/management/commands/fetch_external_data.py
import requests
from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Fetches data from an external API and caches the result.'

    def handle(self, *args, **options):
        films_api_url = 'https://ghibli.rest/films'

        try:
            response = requests.get(films_api_url)
            response.raise_for_status()
            films_list = response.json()

            # Cache the result for 1 minute (60 seconds)
            cache.set('get_all_films', films_list, 60)

            self.stdout.write(self.style.SUCCESS('Successfully fetched and cached external data.'))

        except requests.RequestException as e:
            # Handle request errors (e.g., connection error, timeout)
            self.stdout.write(self.style.ERROR(f'Error fetching external data: {str(e)}'))

        except Exception as e:
            # Handle other unexpected errors
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
