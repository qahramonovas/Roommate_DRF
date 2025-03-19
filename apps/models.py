from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextChoices, PositiveIntegerField, EmailField, Model, ImageField, IntegerField, \
    ForeignKey, CASCADE, FileField, TextField, SET_NULL, SmallIntegerField, DateTimeField, ManyToManyField
from django.db.models import Model, CharField, ForeignKey, CASCADE, SET_NULL, ImageField, BooleanField, TextField, \
    IntegerField, DateTimeField, EmailField, FloatField, TextChoices


class CustomUserManager(BaseUserManager):
    def _create_user(self,  email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        email = GlobalUserModel.normalize_username(email)
        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user( email, password, **extra_fields)





#   =========================================================
class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name




#   =========================================================
class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='districts')

    def __str__(self):
        return self.name




#   =========================================================
class Gender(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name




#   =========================================================
class User(AbstractUser):
    class UserRole(TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        RENTER = 'renter', 'Renter'
    objects = CustomUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    first_name = CharField(max_length=255, null=True, blank=True)
    last_name = CharField(max_length=255, null=True, blank=True)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=12, null=True, blank=True)
    gender = ForeignKey('apps.Gender',on_delete=SET_NULL, null=True, related_name='users')
    university = ForeignKey('apps.University',on_delete=CASCADE, related_name='users', null=True, blank=True)
    password = CharField(max_length=10)
    image = ImageField(upload_to='media/users/', null=True, blank=True)
    invisible = BooleanField(default=False, null=True, blank=True)
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='users', null=True, blank=True)
    district = ForeignKey('apps.District', on_delete=CASCADE, related_name='users', null=True, blank=True)
    role = CharField(max_length=255, null=True, blank=True, choices=UserRole.choices, default=UserRole.USER)




#   =========================================================
class University(Model):
    name = CharField(max_length=255)
    acronym = CharField(max_length=255)
    longitude = FloatField()
    latitude = FloatField()

    def __str__(self):
        return self.name



# ======================================================
class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name



# ============================================
class Rent(Model):
    name = CharField(max_length=255)
    description = TextField()
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='rents')
    contract = BooleanField()
    broker = BooleanField()
    room_count = IntegerField()
    total_price = FloatField()
    student_jins = ForeignKey('apps.Gender', on_delete=SET_NULL, null=True)
    student_count = IntegerField()
    renter = ForeignKey('apps.User', on_delete=CASCADE, related_name='rents')
    location = CharField(max_length=255)
    longitude = FloatField()
    latitude = FloatField()
    wifi = BooleanField()
    conditioner = BooleanField()
    washing_machine = BooleanField()
    TV = BooleanField()
    refrigerator = BooleanField()
    furniture = BooleanField()
    other_convenience = TextField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# =================================================
class Rate(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='rates')
    rent = ForeignKey('apps.Rent', on_delete=CASCADE, related_name='rates')
    rate = IntegerField()
    comment = TextField()


# ===============================================
class Wishlist(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='wishlists')
    rent = ForeignKey('apps.Rent', on_delete=CASCADE, related_name='wishlists')



#=============================================
class Image(Model):
    rent = ForeignKey('apps.Rent', on_delete=CASCADE, related_name='images')
    url = ImageField(upload_to='media/rent_images')
    hashcode = CharField(max_length=255, unique=True)




#==================================================
class AnnouncementType(Model):
    type = CharField(max_length=255)



#==============================================
class Announcement(Model):
    title = CharField(max_length=255)
    description = TextField()
    type = ForeignKey('apps.AnnouncementType', on_delete=CASCADE, related_name='announcements')
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='announcements')



#=====================================================
class Role(Model):
    name = CharField(max_length=25)

    def __str__(self):
        return self.name


#=====================================================
class Staff(Model):
    firstname = CharField(max_length=255)
    lastname = CharField(max_length=255)
    phone = CharField(max_length=15, unique=True)
    password = CharField(max_length=255)
    role = ForeignKey('apps.Role', on_delete=CASCADE, related_name='staffs')
    email = EmailField(unique=True)
    registered_at = DateTimeField(auto_now_add=True)
    last_login = DateTimeField(auto_now=True)


