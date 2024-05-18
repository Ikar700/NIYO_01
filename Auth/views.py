from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from .serializers import UserSerializer

from datetime import datetime, timedelta

# Create your views here.
class LoginView(APIView):
    
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Setting the refresh token in a cookie
            response = Response({
                'access': access_token,
                'refresh': refresh_token,
                'user': UserSerializer(user).data,
            })

            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                expires=datetime.now() + timedelta(days=7),  # The expiration date for the cookie
                httponly=True,  # The cookie accessible only by the server
                secure=True,  # Ensuring the cookie is only sent over HTTPS
                samesite='Strict'  # Setting the SameSite policy to prevent CSRF attacks
            )
            return response
        else:
            return Response({'error': 'Your Password or Username is incorrect'}, status=401)