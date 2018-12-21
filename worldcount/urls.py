from django.urls import path
from.import views
urlpatterns=[
path('', views.homepage, name='home'),
path('countsss/',views.counted, name='Count'),
path('aboutus/',views.aboutus, name='aboutus')
]
