from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),          # for get and post request. for insert operation. 
    path('<int:id>/', views.employee_form,name='employee_update'),  # for  get and post request. for update operatiion.
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'), # for deleting operation.
    path('list/',views.employee_list, name='employee_list')         # for get request. to retrive nad display all records.
]
