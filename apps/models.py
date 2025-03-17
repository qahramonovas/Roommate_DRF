from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE


class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return Region.name




class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='districts')