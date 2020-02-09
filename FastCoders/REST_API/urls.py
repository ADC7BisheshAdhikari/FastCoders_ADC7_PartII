from django.urls import path
from .views import view_get_post_company
from .views import view_getByID_updateByID_deleteByID

urlpatterns = [
    path('companyApis/',view_get_post_company),
    path('companyApis/<int:ID>',view_getByID_updateByID_deleteByID),
]