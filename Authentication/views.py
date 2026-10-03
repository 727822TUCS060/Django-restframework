from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
from .serializers import *
class UserView(APIView):
    def post(self ,request):
        new_user=User(username=request.data['username'],is_superuser=request.data['is_superuser'],first_name=request.data['first_name'],last_name=request.data['last_name'],phone_number=request.data['phone_number'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response("User Created")
#user validation
class UserLoginView(APIView):
    def post(self ,request):
        """
        user_verify=authenticate(username=request.data['username'],password=request.data['password'])
        if user_verify == None:
            return Response("incorrect username or password try again")
        else:
            return Response("login sucess")
        """
        #custom data using jwt 
        user_data=CustomToken_Serializer(data=request.data)
        if user_data.is_valid():
            return Response(user_data.validated_data)
        else:
            return Response(user_data.errors)

