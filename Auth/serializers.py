from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer

from .models import UserAccount

"""
Serializers for user accounts.

This module defines custom serializers for creating and retrieving user accounts,
extending the serializers provided by the Djoser library.
"""

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    """
    Serializer for creating new user accounts.

    This serializer extends the UserCreateSerializer provided by Djoser
    and is used for creating new user accounts.
    """

    class Meta(UserCreateSerializer.Meta):
        """
        Meta class for the UserCreateSerializer.

        Defines the model and fields to be included in the serialized
        representation when creating a new user account.
        """
        model = UserAccount
        fields = '__all__'


class UserSerializer(UserSerializer):
    """
    Serializer for retrieving user account information.

    This serializer extends the UserSerializer provided by Djoser
    and is used for retrieving user account information.
    """

    class Meta:
        """
        Meta class for the UserSerializer.

        Defines the model and fields to be included in the serialized
        representation when retrieving user account information.
        """
        ref_name = 'AccountsUserSerializer'
        model = UserAccount
        fields = "__all__"
