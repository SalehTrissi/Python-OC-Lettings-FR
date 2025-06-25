from django.urls import path
from . import views

# Defines the URL namespace for the lettings app
app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
