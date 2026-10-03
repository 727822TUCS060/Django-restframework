from rest_framework.views import APIView #create API
from rest_framework.response import Response #send the response to the fontend
from .models import *
from .serializers import *
from django.db.models import Avg ,Min ,Max ,Sum ,Q,Count
from rest_framework.viewsets import ModelViewSet
class StudentAPI(APIView):
    def get(self ,request):
        """
        all_students=Student.objects.all() #it is error format send to the frontend 
        student_list =[] #to store the details
        for s in all_students: #convert to json format
            student_dict={
                "name":s.name, #fields using in model
                "age":s.age,
                "grade":s.grade,
                "is_active":s.is_active
            }
            student_list.append(student_dict)
        return Response(student_list)
        """
       # Student.objects.create(name="kishore", age=22 ,grade="12th")
        #one_students=Student.objects.get(name="kishore",age=23)     #get method use to get only one data by using specific condition
        #first_student =Student.objects.first() #first data
        #last_student=Student.objects.last() #last data
        #all_student=Student.objects.all().order_by('age') #arrange based on one field in ascending order for descending use - (-id)
        #student_data=Student_Serializer(all_student ,many=True).data

        #return Response(student_data)
        #data=Student.objects.aggregate(Sum('age')) #for aggregate functions
        #filter_data=Student.objects.filter(is_active="False")#filter based on criteria and it does not give error message for the data not found it gives the empty list and use the multiple field 
        #exclude_data=Student.objects.filter(grade="A+").exclude(is_active="False")#filter based on criteria and exclude some data based on criteria
        #number_data=Student.objects.filter(age__lte=23)#filter based on number data 
        #__gte is greater than or equal to 
        #range_data=Student.objects.filter(joined_date__range=("2026-09-29","2026-09-30")) #range based data
       # date_year=Student.objects.filter(joined_date__day='29') #filter based on month ,year and date
        #multiple_match_data=Student.objects.filter(name__in=['dhanush','pragadesh'])
        #student_data=Student_Serializer(multiple_match_data ,many=True).data
        #author=Author.objects.filter(books__published_year=2010) #books is related name
        #author_count=Author.objects.annotate(book_count=Count('books'))
        #data=Author_Serializer(author_count ,many=True).data
        """ for a in author_count:
            print(a.name , a.book_count) 
        """
        #book_data=Book.objects.filter(author=7) #author is foreign key field name to find name but for id use the field name only 
        book_data =Book.objects.get(id=4)
        print(book_data.title)
        print(book_data.author)
        print(book_data.published_year)
        print(book_data.author.name)
        #data=Book_Serializer(book_data , many=True).data
        return Response()
    def post(self, request):
        print(request.data) #to store the data
        new_student=Student(name = request.data['name'],age=request.data['age'],grade=request.data['grade'],is_active=request.data['is_active'],joined_date=request.data['joined_date']) #key values from model field 
        new_student.save()
        return Response("New Student Created Successfully")
    def patch(self ,request ,student_id):
        print(student_id , "student_id")
        student_data=Student.objects.filter(id=student_id) #filter is use to match the rows and columns in the model

        print(student_data)
        student_data.update(name = request.data['name'],age=request.data['age'],grade=request.data['grade'],is_active=request.data['is_active'],joined_date=request.data['joined_date'])
        return Response("Data") 
class Authorapi(APIView):
    def post(self ,request):
        new_author=Author(name=request.data['name'])
        new_author.save()
        return Response("Author name added successfully")
    def delete(self , request , id): #delete uses manual method
        author=Author.objects.get(id=id)
        author.delete()
        return Response("author Deleted")


class Bookapi(APIView):
    def post(self, request):
        author_id = request.data.get('author')

        try:
            author_obj = Author.objects.get(id=author_id)
        except (Author.DoesNotExist, ValueError, TypeError):
            return Response(
                {"error": "Author ID does not exist"},
            )

        new_book = Book.objects.create(
            title=request.data.get('title'),
            author=author_obj,
            published_year=request.data.get('published_year', 0)
        )

        return Response(
            {
                "message": "Book added successfully",
                "id": new_book.id,
                "title": new_book.title,
                "author": author_obj.name,
                "author_id": author_obj.id,
                "published_year": new_book.published_year
            })
    def delete(self , request , id): #delete uses manual method
        book=Book.objects.get(id=id)
        book.delete()
        return Response("Book Deleted")
class ProfileView(ModelViewSet):
    queryset=profile.objects.all()
    serializer_class=ProfileSerializer
class UserProfileView(APIView):
    def post(self ,request):
        try:
            new_profile=profile(user_id=request.data['user'],bio=request.data['bio'])
            new_profile.save()
            return Response("Profile Created")
        except:
            return Response("The user already have a profile")



    