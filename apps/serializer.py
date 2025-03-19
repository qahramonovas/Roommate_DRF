from django.contrib.auth.hashers import make_password
from rest_framework.fields import EmailField, CharField, IntegerField, BooleanField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import User



class UserSerializer(Serializer):
    email = EmailField(max_length=255)
    code = CharField(max_length=5, min_length=5)

class UserRegisterSerializer(Serializer):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number =  CharField(max_length=255)
    gender_id = IntegerField()
    university_id = IntegerField()
    invisible = BooleanField
    region_id = IntegerField()
    district_id = IntegerField()
    email = EmailField()
    password = CharField(max_length=5, min_length=5)

    def validate_password(self, value):
        return make_password(value)


class EmailSerializer(Serializer):
    email = CharField(max_length=255)