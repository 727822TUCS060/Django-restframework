from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("profile",ProfileView)
urlpatterns=[
    path('student/',StudentAPI.as_view()),
    path('student/<student_id>/',StudentAPI.as_view()),
    path('Author/',Authorapi.as_view()),
    path('book/',Bookapi.as_view()),
    path('Author/<id>/',Authorapi.as_view()),
    path('book/<id>/',Bookapi.as_view()),
    path('',include(router.urls)),
    path('api/',UserProfileView.as_view())
    

]