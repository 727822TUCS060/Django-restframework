from django.db import models

# Create your models here.
#password Kishore007$$
#to delete remove all fields and table name in the model and rerun the migrations and migrate to delete the table in the sql
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=1)
    def __str__(self):
            return self.name 
class Task(models.Model):
    student_reference = models.ForeignKey(Student,related_name= 'all_task',null=True,on_delete=models.CASCADE)#model should above the foreignkey and one model can use and ondelete uses cascade deletes the student data with task data ,if uses set null the student deletes and task won't delete  and to give the details use the foreign key model id details which are existing 
    #in this related_name is used to display the child details in the parent
    task_name = models.CharField(max_length=200)
    description=models.TextField()
class ranksheet(models.Model):
     tamil=models.IntegerField()
     English=models.IntegerField()
     Maths=models.IntegerField()
     Science=models.IntegerField()
     social_science=models.IntegerField()
     total=models.IntegerField()
     average=models.FloatField()
     rank=models.BooleanField()
   #to display string in the admin table