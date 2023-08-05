**Crear entorno virtual**
```python -m venv env```


**Activar entorno virtual**
```env\Scripts\activate```

**Instalar Django**
```pip install django```

**Crear proyecto**
```django-admin startproject simple_blog```

**Crear app**
```python manage.py startapp blog```

**Crear usuario para admin**
```python manage.py createsuperuser```

**Para que las migraciones se apliquen, y no de guerra con la bd de sqlite.**
```python manage.py migrate```

**Correr servidor**
```python manage.py runserver```

