from django.urls import path
from home.views import HomeIndex

urlpatterns = [
    path('', HomeIndex.as_view()),
]