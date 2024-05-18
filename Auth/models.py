from django.db import models
from django.contrib.auth.models  import BaseUserManager, AbstractBaseUser, PermissionsMixin

from uuid import uuid4

class UserAccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('You must have an email to sign up')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          **extra_fields
                        )
        user.set_password(password)
        
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):

        user =self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True

        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    email= models.EmailField(max_length=55, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name',
                        'last_name',
                        'username']

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name