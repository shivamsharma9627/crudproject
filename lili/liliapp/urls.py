from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('add_student',views.add_student,name="add_student"),
    path('edit_student/<int:roll>',views.edit_student,name="edit_student"),
    path('do_edit_student/<int:roll>',views.do_edit_student,name="do_edit_student"),
    path('delete_student/<int:roll>',views.delete_student,name="delete_student"),

  
]
