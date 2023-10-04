from django.urls import path
from . import views

urlpatterns = [
    path('', views.Demo, name='Home'), 
    path('Addemployee', views.Adddemployee, name='Addemployee'),
    path('Display', views.Display, name='Display'),
    path('delete/<str:employee_id>/', views.delete, name='delete'),
    path('update/<str:employee_id>/', views.update, name='update'),
    path('view/<str:employee_id>/', views.view, name='view'),
    path('search/',views.search,name="search"),

]
