from django.db import models
from datetime import datetime


class Visitor(models.Model):

    name_visitor = models.TextField(unique=True, max_length=30)

    is_welcome = models.BooleanField(default=False)

    date_visit = models.DateTimeField(default=datetime.now())
