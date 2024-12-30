
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index,name='login_view'),
    path('signup',signupview,name='signup_view'),
    path('patienthome',patient_home,name='patient_home_view'),
    path('logout',logoutview,name='logout_view'),
    path('adddiet',add_diet,name='diet_view'),
    path('deldiet', delete_diet_view, name='deldiet'),
    path('editdiet', edit_diet_view, name='editdiet'),

]
