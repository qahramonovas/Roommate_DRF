from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, SET_NULL, ImageField, BooleanField
from django.db.models.fields import FloatField


#   =========================================================
class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return Region.name




#   =========================================================
class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='districts')

    def __str__(self):
        return District.name




#   =========================================================
class Gender(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return Gender.name




#   =========================================================
class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number = CharField(max_length=12)
    gender = ForeignKey('apps.Gender',on_delete=SET_NULL, null=True, related_name='users')
    university = ForeignKey('apps.University',on_delete=CASCADE, related_name='users')
    password = CharField(max_length=10)
    image = ImageField(upload_to='media/users/')
    invisible = BooleanField(default=False)
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='users')
    district = ForeignKey('apps.District', on_delete=CASCADE, related_name='users')


    def __str__(self):
        return User.name



#   =========================================================
class University(Model):
    name = CharField(max_length=255)
    acronym = CharField(max_length=255)
    longitude = FloatField()
    latitude = FloatField()

    def __str__(self):
        return University.name

