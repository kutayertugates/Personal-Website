from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.Index, name='List'),
    path('<slug:slug>', views.Detail, name='Detail')
]