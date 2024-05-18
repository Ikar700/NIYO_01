from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer

from .models import UserAccount

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        
        model = UserAccount
        fields = '__all__'


class UserSerializer(UserSerializer):

    class Meta:
        ref_name = 'AccountsUserSerializer'
        model = UserAccount
        fields = "__all__"