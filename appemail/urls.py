from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.hello_world, name='hello_world'),
    path('/',views.home_page, name='home_page')
]
