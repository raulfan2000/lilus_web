from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
import inicio.models
import inspect

for model in inspect.getmembers(inicio.models, inspect.isclass):
    if models.Model in inspect.getmro(model[1]) and not model[1] is User:
        admin.site.register(model[1])
