# My notes throughout the course

## Django-admin commands

### Setup project

`django-admin startproject <proj name>`

### Start server (preview)

`python3 manage.py runserver`

### Create app in project

`python3 manage.py startapp <app name>`

### Create models migration

`python3 manage.py makemigrations`

### Migrate models to db

`python3 manage.py migrate`

### Shell

`python3 manage.py shell`

## Notes for models in shell

### Get all objects for model (import model first) 

`<model>.objects.all()`

### Save model (create model first)

`<obj>.save()`

### Delete model

`<obj>.delete()`

### Create and save

`<model>.objects.create(**kwargs)`

### Get obj of model by id or attr (always gets only 1 entry; error when more values -- use only on UQ)

`<model>.objects.get(<id or attr>)`

### Filter models by attrs

`<model>.objects.filter(<attr>=<val>, ...)`

### Query filters (modifiers like lt, ge, etc.)

`<models>.objects.filter(<attr>__<modifier>=<val>)`
Book.objects.filter(rating__lt=3, title__contains='Story')

### Query filters with logical operators (| - or; , - and)

```
from django.db.models import Q
Book.objects.filter(Q(<attr>__<mod>=<val>) | Q(<attr>=<val>))
Book.objects.filter(Q(<attr>__<mod>=<val>) | Q(<attr>=<val>), <attr>=<val>)
```
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), author="J.K. Rowling")

#### Storing in a variable caches query, doesn't hit db mutliple times