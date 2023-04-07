from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    ID_number=models.CharField(max_length=254,unique=True,primary_key=True, blank=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email

class Care_giver(models.Model):
    ID= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    ID_number=models.ForeignKey("User", to_field='ID_number', on_delete=models.CASCADE)
    address= models.CharField(max_length=254, null=True, blank=True)
    contact= models.CharField(max_length=254, null=True, blank=True)
    surety_name= models.CharField(max_length=254, null=True, blank=True)
    surety_IDnumber= models.CharField(max_length=254, null=True, blank=True)
    years_of_exprience= models.IntegerField()
    question= models.CharField(max_length=254, null=True, blank=True)
    def __str__(self):
        return str(self.email)

