
from django.urls import path
from crud_app import views

urlpatterns = [
    path('display/',views.display_data,name='display'),
    path('add_data/',views.create_data,name='add_data'),
    path('update_data/<int:emp_id>/',views.update_data,name='update_data'),
    
    
]