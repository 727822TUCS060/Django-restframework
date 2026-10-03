from rest_framework.routers import DefaultRouter
from .views import BookView

book_router=DefaultRouter()

book_router.register(r'book' ,BookView)