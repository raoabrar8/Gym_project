from django.urls import path
from .views import *
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('reports/', Reports, name='reports'),
    path('manage_members/', manage_members, name='manage_members'),
    path('member_details/<int:id>', member_details, name='member_details'),
    path('add_member/', add_member, name='add_member'),
    path('update_member/<int:id>', update_member, name='update_member'),
    path('delete_member/<int:id>', delete_member, name='delete_member'),
]
