from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index), #127.0.0.1/myapp/index
    path('show_int/<int:value>',show_int) #127.0.0.1/myapp/show_int/<value>
]