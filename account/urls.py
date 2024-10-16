from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
     path('notavailable/', views.notavailable, name='notavailable'),
    path('certificate/', views.certificate, name='certificate'),
    path('certificate_login/', views.certificate_login, name='certificate_login'),
]
