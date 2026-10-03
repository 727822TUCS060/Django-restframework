from django.urls import path
from  .views import * #* for all class

urlpatterns=[
    path('student/',StudentAPI.as_view()),
    path('student/<int:student_id>/',StudentAPI.as_view()),
    path('task/',TaskView.as_view()),
    path('task/<int:task_id>/',TaskView.as_view()),
    path('rank/',RanksheetView.as_view()),
    path('rank/<int:id>/',RanksheetView.as_view()),
    path('task_list/',task_list_create),
    path('task_id/<int:id>/',task_update_delete),


    
]