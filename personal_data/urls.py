from django.urls import path
from . import views

urlpatterns = [
    path('api/people/', views.get_people, name='get-people'),
    path('api/people/<str:nin>/', views.get_person, name='get-person'),
]
