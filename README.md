## Functionalities Implemented
1. Get all films API: API returns data of all films including actors data such as name, id etc.
2. Caching in API: In every 1 minute, data should be cached. Hence we don't need to call internal API everytime.
3. Authenticating the API: API is authenticated via a secret key.
4. Test cases: We can test whether API will run in certain conditions or not such as: when secret key is passed, not passed or passed incorrectly.

## Install packages
Run command `pip install django djangorestframework requests celery redis`.

## How to start app?
Run command `python manage.py runserver`.

How to run API?
1. Open Postman
2. Add a header `Authorization` with value `ghiblikey`.
2. Call API `GET http://127.0.0.1:8000/api/get_all_films/`.
4. It should return the result.

## How to run tests?
Simply run command `python manage.py test myapp`

## Improvements
1. Add secret key in env variable so that it is not exposed.
2. All packages in app should be installed without specifically mentioning each one of them.