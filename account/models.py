from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        extra_fields.setdefault('is_active',True)
        if not phone_number:
            raise ValueError("User Must Phone Number")
        
        user = self.model(phone_number=phone_number,**extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_author = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    
    
    
    def __str__(self):
        return self.phone_number