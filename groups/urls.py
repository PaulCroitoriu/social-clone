from django.urls import path
from .import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('post/in/<slug:slug>/', views.SingleGroup.as_view(), name='single'),
    path('new/', views.CreateGroup.as_view(), name='new'),
    path('join/<slug:slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveGroup.as_view(), name='leave'),
]
