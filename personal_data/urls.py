from django.urls import path
from . import views

urlpatterns = [
    path('api/people/', views.PersonList.as_view(), name='person-list'),
    path('api/people/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
]
