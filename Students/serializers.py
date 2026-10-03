from rest_framework.serializers import ModelSerializer
from .models import Task , ranksheet , Student
class Student_Serializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class Task_serializer(ModelSerializer): #can create multiple serailizer
    class Meta: #which model is used
        model=Task
        fields='__all__' # for all fields
class Ranksheet_Serializer(ModelSerializer):
    class Meta:
        model =ranksheet 
        fields= '__all__'
        #fields=['task_name'] #for specific field 
class Task_data_serializer(ModelSerializer): #to get the reference id values(data)
    student_reference=Student_Serializer()#inheriting parent serializer
    class Meta: #which model is used
        model=Task
        fields='__all__' # for all fields
class Student_task_Serializer(ModelSerializer): #to show tasks for student
    all_task=Task_serializer(many=True)#to show the details of the child in the parent
    class Meta:
        model=Student
        fields='__all__'


