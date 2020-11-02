from django.db import models


class HTTPMethods(models.TextChoices):
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
