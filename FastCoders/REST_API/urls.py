from django.urls import path
from .views import view_get_post_airport
from .views import view_getByID_updateByID_deleteByID

urlpatterns = [
    path('companyapis/',view_get_post_airport),
    path('companyapis/<int:ID>',view_getByID_updateByID_deleteByID),
]