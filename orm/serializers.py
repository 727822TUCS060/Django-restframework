from rest_framework.serializers import ModelSerializer
from .models import *
class Student_Serializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class Author_Serializer(ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
class Book_Serializer(ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class Authorwithbook_Serializer(ModelSerializer):
    books=Book_Serializer(many=True)
    class Meta:
        model=Author
        fields='__all__'
class BookwithAuthor_Serializer(ModelSerializer):
    author=Author_Serializer()
    class Meta:
        model=Book
        fields='__all__'
class ProfileSerializer(ModelSerializer):
    class Meta:
        model=profile
        fields=['id','user','bio']
