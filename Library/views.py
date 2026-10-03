from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import generics
from .serializers import *
from .models import *

generics.CreateAPIView #post the data
generics.ListAPIView #get all dataa
generics.RetrieveAPIView #get by id
generics.UpdateAPIView #update particular
generics.DestroyAPIView #delete data
generics.ListCreateAPIView #post and get all
generics.RetrieveDestroyAPIView #getby id ,delete
generics.RetrieveUpdateAPIView #get by id ,update
generics.RetrieveUpdateDestroyAPIView #get by id ,update ,delete
class BookView(ModelViewSet):
    queryset= Book.objects.all() #to pass get all data
    serializer_class = Book_Serializer #serailizer 
class LaptopView(generics.ListCreateAPIView):#post and get all data
    def get_queryset(self):
        return Laptops.objects.filter(brand='hcl')
    def perform_create(self, serializer):
        serializer.save(user_type='office')
    queryset=Laptops.objects.all()
    serializer_class=Laptop_Serializer #can create the url directly
class LaptopViewById(generics.RetrieveUpdateDestroyAPIView):#get by id ,update adn delete
    queryset=Laptops.objects.all()
    serializer_class=Laptop_Serializer
    def perform_update(self, serializer):
            serializer.save(user_type='Home')
 
# Create your views here.
