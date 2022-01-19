from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  # path('dashboard', views.dashboard, name='dashboard'),
  path('deposit', views.deposit, name='deposit'),
  path('fusionhub', views.fusionhub, name='fusionhub'),
  # path('signin', views.signin, name='signin'),
  # path('signup', views.signup, name='signup'),
  path('withdraw', views.withdraw, name='withdraw'),
  # path('logout', views.logout, name='logout'),
]
