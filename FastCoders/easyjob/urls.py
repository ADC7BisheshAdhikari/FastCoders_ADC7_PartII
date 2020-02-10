from django.contrib import admin  
from django.urls import path  
from easyjob import views  
from .views import applicant, firstPage
from .views import *

urlpatterns = [   
    path('company/', views.emp, name="company"),  
    path('show',views.show, name="show"),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('search/',views.search, name="search"),
    path('base/',base,name="base"),  

  
] 


urlpatterns += [
    path('profile/',applicant, name="profile"),
<<<<<<< Updated upstream
    path('',firstPage, name="index"),    
=======
    path('',firstPage, name="index"),
    
  
    
>>>>>>> Stashed changes
]


