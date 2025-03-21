from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insertField/', views.add_field,),
    path('update/<int:id>/', views.update_field),
    path('update/<int:id>/update/', views.update_field),
    path('deleteField/<int:id>/', views.deleteField)
]