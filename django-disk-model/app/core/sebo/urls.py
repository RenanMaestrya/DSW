from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('disk/<int:pk>', disk, name='disk'),
    path('registerDisk/', registerDisk.as_view(), name='registerDisk'),
    path('editDisk/<int:pk>', EditDisk.as_view(), name='editDisk'),
    path('deleteDisk/<int:pk>', DeleteDisk.as_view(), name='deleteDisk'),
]