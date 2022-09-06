from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('units/',views.units,name='units'),
    path('currencies/',views.currencies,name='currencies'),
    path('atten_prod/',views.atten_prod,name='atten_prod'),
    path('emp_groups/',views.emp_groups,name='emp_groups'),
    path('employee/',views.employee,name='employee'),
]