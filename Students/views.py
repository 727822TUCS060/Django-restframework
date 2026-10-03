from rest_framework.views import APIView #create API
from rest_framework.response import Response #send the response to the fontend
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from decouple import config
class StudentAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self ,request):
        all_students=Student.objects.all() #it is error format send to the frontend 
        student_data=Student_task_Serializer(all_students , many=True).data
        #student_list =[] #to store the details
        #for s in all_students: #convert to json format
           # student_dict={
            #    "id":s.id,
            #    "name":s.name, #fields using in model
             #   "age":s.age
            #}
            #student_list.append(student_dict)
        
        return Response(student_data)
    
    def post(self, request):
        print(request.data) #to store the data
        new_student=Student(name = request.data['name'],age=request.data['age']) #key values from model field 
        new_student.save()
        return Response("New Student Created Successfully") 
    def patch(self ,request ,student_id):
        print(student_id , "student_id")
        student_data=Student.objects.filter(id=student_id) #filter is use to match the rows and columns in the model

        print(student_data)
        student_data.update(name = request.data['name'],age=request.data['age'])
        return Response("Data")
    def delete(self ,request ,student_id):
        student_data =Student.objects.get(id = student_id) #get to select the data
        student_data.delete()
        return Response("delete")

class TaskView(APIView): #all data api
    def get(self , request,task_id=None): #method name is only once used if two use the second only applicable
        if task_id == None: #get all details
            person_name=config('name')#key name from env file
            print(person_name)
            all_task =Task.objects.all()
            task_data = Task_data_serializer(all_task, many=True).data#convert readable format 
            return Response(task_data)
        else: #get the details for particular id 
            task =Task.objects.get(id=task_id)
            task_data = Task_data_serializer(task).data#convert readable format 
            return Response(task_data)
    def post(self , request):
        new_task = Task(student_reference_id=request.data['student_reference'],task_name=request.data['task_name'],description=request.data['description'])
        new_task.save()
        return Response("New Task Added")
        """
        new_task=Task_serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)
        """
    def put(self ,request ,task_id):
        task=Task.objects.get(id=task_id)
        task_update=Task_serializer(task , data=request.data , partial=True) #send the updated field value 
        if task_update.is_valid():
            task_update.save()
            return Response("Task Updated")
        else:
            return Response(task_update.errors)
    def delete(self , request , task_id): #delete uses manual method
        task=Task.objects.get(id=task_id)
        task.delete()
        return Response("Task Deleted")
class RanksheetView(APIView): #use manual method for logical calculation
    def get (self ,request ,id=None):
        if id == None:
            all_rank=ranksheet.objects.all()
            rank_data =Ranksheet_Serializer(all_rank ,many=True).data
            return Response(rank_data)
        else:
            rank=ranksheet.objects.get(id=id)
            rank_data=Ranksheet_Serializer(rank).data
            return Response(rank_data)

    def post(self ,request):
        total_marks=request.data['tamil']+request.data['English']+request.data['Maths']+request.data['Science']+request.data['social_science']
        average_marks=total_marks/5
        if (request.data['tamil']>=35 ) and (request.data['English']>=35 ) and (request.data['Maths']>=35 ) and (request.data['Science']>=35 ) and (request.data['social_science']>=35 ):
            student_result=True
        else:
            student_result =False
        new_data = ranksheet(tamil=request.data['tamil'],English=request.data['English'],Maths=request.data['Maths'],Science=request.data['Science'],social_science=request.data['social_science'],total=total_marks,average=average_marks , rank=student_result)
        new_data.save()
        return Response("Data saved")
    def put(self ,request ,id):
        
        total_marks=request.data['tamil']+request.data['English']+request.data['Maths']+request.data['Science']+request.data['social_science']
        average_marks=total_marks/5
        if (request.data['tamil']>=35 ) and (request.data['English']>=35 ) and (request.data['Maths']>=35 ) and (request.data['Science']>=35 ) and (request.data['social_science']>=35 ):
            student_result=True
        else:
            student_result =False
        rank_data=ranksheet.objects.filter(id=id) #filter is use to match the rows and columns in the model
        print(rank_data)
        rank_data.update(tamil=request.data['tamil'],English=request.data['English'],Maths=request.data['Maths'],Science=request.data['Science'],social_science=request.data['social_science'],total=total_marks,average=average_marks , rank=student_result)
        return Response("Data")
    def delete(self , request , id): #delete uses manual method
            rank=ranksheet.objects.get(id=id)
            rank.delete()
            return Response("Data Deleted")
@api_view(['GET','POST'])
def task_list_create(request):
    if request.method =='GET':
        all_task =Task.objects.all()
        task_data = Task_serializer(all_task, many=True).data#convert readable format 
        return Response(task_data)
    elif request.method =='POST':
        new_task=Task_serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)
@api_view(['GET','PUT','DELETE'])
def task_update_delete(request ,id):
    task=Task.objects.get(id=id)
    if request.method== 'GET':
        task_data = Task_serializer(task).data#convert readable format 
        return Response(task_data)
    elif request.method =='PUT':
        task_update=Task_serializer(task , data=request.data , partial=True) #send the updated field value 
        if task_update.is_valid():
            task_update.save()
            return Response("Task Updated")
        else:
            return Response(task_update.errors)
    elif request.method =='DELETE':
        task.delete()
        return Response("Task Deleted")




    
    



   

