python manage.py dumpdata restaurants --output restaurants/seeds.json --indent=2;
python manage.py dumpdata dog_friendly --output dog_friendly/seeds.json --indent=2;
python manage.py dumpdata reviews --output reviews/seeds.json --indent=2;
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;