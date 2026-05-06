from django.urls import path
from.views import *

urlpatterns = [
    path('',home),
    path('add/',add),
    path('details/',details),
    path('details/<int:id>/',emp_delete,name='employee_delete'),
    path('add/<int:id>/',emp_update,name= 'employee_update'),

]