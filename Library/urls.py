from django.urls import path  , include
from .router import book_router
from .views import *
urlpatterns=[
    path('api/',include(book_router.urls)),
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/',LaptopViewById.as_view()) #id name is pk as default (primary key)

]