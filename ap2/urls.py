from django.urls import path
from . import views
urlpatterns=[
    path('members/',views.members, name='members'),
    path('testing/',views.testing, name='testing'),
    path('testing1/',views.testing1,name='testing1'),
    path('testing2/',views.testing2,name='testing2'),
    path('showlist/',views.showlist,name='showlist'),
]