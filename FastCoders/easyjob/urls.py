from django.contrib import admin  
from django.urls import path  
from easyjob import views  
from .views import applicant, firstPage
from .views import *

urlpatterns = [   
    path('company/', views.create_Records, name="company"),  
    path('show',views.show_Records, name="show"),  
    path('edit/<int:id>', views.edit_Records),  
    path('update/<int:id>', views.update_Records),  
    path('delete/<int:id>', views.destroy_Records),
    path('search/',views.search, name="search"),
    path('base/',base,name="base"),  

  
] 


urlpatterns += [
    path('profile/',applicant, name="profile"),
    path('',firstPage, name="index"),    
]


