from django.urls import path

from . import views


#app_name="main"
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('signup/', views.signup, name='signup'),


    path('analize/<i>/',views.analize,name="analize"),
    path('analizekey/',views.analizekey,name="analizekeyword"),

    path('logout/',views.logout_request,name="logout")


]
