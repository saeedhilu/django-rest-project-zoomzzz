from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from pytz import timezone
from .managers import UserManager
from datetime import timedelta, datetime
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework
from django.db.models.functions import Now
phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be 10 digits only',
)

class User(AbstractBaseUser, PermissionsMixin):
    email        = models.EmailField(_('email address'), unique=True, null=True, blank=True) 
    phone_number = models.CharField(max_length=10, validators=[phone_regex], unique=True, null=True, blank=True)
    username     = models.CharField(max_length=50, unique=True, null=True, blank=True)
    first_name   = models.CharField(max_length=50, blank=True, null=True)
    last_name    = models.CharField(max_length=50, blank=True, null=True)
    is_vendor    = models.BooleanField(default=False)
    date_joined  = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)

    objects      = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username or self.phone_number or self.email

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}' 

from django.db import models
from django.utils import timezone

def default_expiry():
    return timezone.now() + timezone.timedelta(minutes=5)

class OTP(models.Model):
    phone_number = models.CharField(max_length=10, validators=[phone_regex], unique=True, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=True) 
    otp_code = models.CharField(max_length=6)
    otp_expiry = models.DateTimeField(default=default_expiry)

    @classmethod
    def create(cls, phone_number, otp_code, otp_expiry):
        return cls.objects.create(phone_number=phone_number, otp_code=otp_code, otp_expiry=otp_expiry)

    def is_expired(self):
        return timezone.now() > self.otp_expiry

    
# OTP.objects.filter(otp_expiry__gte=Now()-timespan(days=1))
