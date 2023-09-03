from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('send_message/', views.send_messages)
    # path('addPerson/', views.add_person),
    # path('openUpdatePerson/<id>', views.open_update_person),
    # path('updatePerson/<id>', views.update_person),
    # path('deletePerson/<id>', views.delete_person),
    # path('visualizePerson/<id>', views.visualize_person)
]