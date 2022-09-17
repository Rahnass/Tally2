from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),

    path('statistics_units/',views.statistics_units,name='statistics_units'),
    path('statistics_unit_alter/<int:pk>',views.statistics_unit_alter,name='statistics_unit_alter'),
    path('statistics_cunit_alter/<int:pk>',views.statistics_cunit_alter,name='statistics_cunit_alter'),
    path('statistics_su_alter/<int:pk>',views.statistics_su_alter,name='statistics_su_alter'),
    path('statistics_cu_alter/<int:pk>',views.statistics_cu_alter,name='statistics_cu_alter'),

    path('statistics_currencies/',views.statistics_currencies,name='statistics_currencies'),
    path('statistics_curr_alter/<int:pk>',views.statistics_curr_alter,name='statistics_curr_alter'),   
    path('statistics_curr_alter2/<int:pk>',views.statistics_curr_alter2,name='statistics_curr_alter2'),
    path('statistics_cdef_alt/<int:pk>',views.statistics_cdef_alt,name='statistics_cdef_alt'),
    path('statistics_curr_alt/<int:pk>',views.statistics_curr_alt,name='statistics_curr_alt'),

    path('statistics_atten_prod/',views.statistics_atten_prod,name='statistics_atten_prod'),
    path('statistics_atten_alt/<int:pk>',views.statistics_atten_alt,name='statistics_atten_alt'),
    path('statistics_atten_alter/<int:pk>',views.statistics_atten_alter,name='statistics_atten_alter'),
    path('statistics_att_create/',views.statistics_att_create,name='statistics_att_create'),
    path('statistics_add_attend/',views.statistics_add_attend,name='statistics_add_attend'),

    path('statistics_emp_groups/',views.statistics_emp_groups,name='statistics_emp_groups'),
    path('statistics_p_cost/<int:pk>',views.statistics_p_cost,name='statistics_p_cost'),
    path('statistics_eg_alt/<int:pk>',views.statistics_eg_alt,name='statistics_eg_alt'),
    path('statistics_pcost_alt/<int:pk>',views.statistics_pcost_alt,name='statistics_pcost_alt'),
    path('statistics_empgrp_alt/<int:pk>',views.statistics_empgrp_alt,name='statistics_empgrp_alt'),
    path('statistics_empg_dtls/<int:pk>',views.statistics_empg_dtls,name='statistics_empg_dtls'),
    path('statistics_create_payhd/',views.statistics_create_payhd,name='statistics_create_payhd'),
    path('statistics_empg_create/',views.statistics_empg_create,name='statistics_empg_create'),
    path('statistics_add_empg/',views.statistics_add_empg,name='statistics_add_empg'),

    path('statistics_employee/',views.statistics_employee,name='statistics_employee'),
    path('statistics_emp_alt/<int:pk>',views.statistics_emp_alt,name='statistics_emp_alt'),
    path('statistics_employee_alt/<int:pk>',views.statistics_employee_alt,name='statistics_employee_alt'),
    



    path('statistics_add_payhead/',views.statistics_add_payhead,name='statistics_add_payhead'),
]