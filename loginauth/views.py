from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class Register(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        qs = User.objects.all()
        serializer = UserSerializer(qs,many=True)
        return Response(serializer.data)