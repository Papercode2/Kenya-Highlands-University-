from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('admission/', views.admission, name='admission'),
    path('login/', views.loginPage, name='login'),
    path('', views.logout, name='logout'),
    path('odel/', views.odel, name='odel'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('success/', views.success, name='success'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('results/', views.results, name='results'),
    path('units/', views.units, name='units'),
    path('nominals/', views.nominals, name='nominals'),
]
