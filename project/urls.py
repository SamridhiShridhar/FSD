"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from ap1.views import current_date_time, find_mode, n_hours, table_of_squares, vote, vowel_consonants
from ap2.views import aboutus, contactus, home, showlist,getpos, getstable
from course_registration.views import insert_demo,update_demo,delete_demo,retreive_demo 
urlpatterns = [
    path('',include('ap2.urls')),
    path('admin/', admin.site.urls),
    path('cdt/', current_date_time),
    path('tos/<int:s>/<int:e>/',table_of_squares),
    path('vowcon/<str:sentence>/',vowel_consonants),
    path('find_mode/<str:listofnum>/',find_mode),
    path('vote/<int:age>/',vote),
    path('nhrs/<int:n>/',n_hours),
    path('',include('ap2.urls')),
    path('showlist/',showlist),
    path('aboutus/',aboutus),
    path('home/',home),
    path('contactus/',contactus), 
    path('registration/', include('course_registration.urls')),
    path('getpos/',getpos),
    path('getstable/', getstable),
    path('insert_demo/', insert_demo),
    path('update_demo/', update_demo),
    path('delete_demo/', delete_demo),
    path('retreive_demo/', retreive_demo),
]
