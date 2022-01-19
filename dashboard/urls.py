from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('dashboard', views.dashboard, name='dashboard'),
  path('deposit', views.deposit, name='deposit'),
  path('payment', views.payment, name='payment'),
  path('signin', views.signin, name='signin'),
  path('signup', views.signup, name='signup'),
  path('withdraw', views.withdraw, name='withdraw'),
  path('profile', views.profile, name='profile'),
  path('hub', views.hub, name='hub'),
  path('fusionform', views.fusionform, name='fusionform'),
  path('hubtrade', views.hubtrade, name='hub-trade'),
  path('logout', views.logout, name='logout'),
]