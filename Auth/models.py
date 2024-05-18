from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from uuid import uuid4

"""
Custom user model and manager for user authentication.

This module defines a custom user model and a user account manager
for handling user authentication and authorization in the application.
"""

# User account manager for custom user
class UserAccountManager(BaseUserManager):
    """
    Custom user account manager for creating and managing user accounts.

    This manager extends the BaseUserManager and provides methods for
    creating regular users and superusers.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new regular user account.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password for the user account.
            **extra_fields: Additional fields for the user account.

        Returns:
            UserAccount: The created user account instance.

        Raises:
            ValueError: If the email address is not provided.
        """

        # Error handling for not email
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
        """
        Creates and saves a new superuser account.

        Args:
            email (str): The email address of the superuser.
            password (str, optional): The password for the superuser account.
            **extra_fields: Additional fields for the superuser account.

        Returns:
            UserAccount: The created superuser account instance.
        """

        user = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    Custom user account model for user authentication and authorization.

    This model extends the AbstractBaseUser and PermissionsMixin classes
    and defines the fields and properties for user accounts.
    """

    # User properties
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=55, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',
                       'last_name',
                       'username']

    def __str__(self) -> str:
        """
        Returns a string representation of the user account.

        Returns:
            str: The user's first name and last name.
        """
        return self.first_name + " " + self.last_name
