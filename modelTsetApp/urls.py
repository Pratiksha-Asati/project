from django.urls import  path
from . import  views

urlpatterns=[
    path("customerDetail/",views.customerModelFormMethod)
]