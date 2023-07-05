from django.urls import path,include
from . import views 
app_name='app4'

urlpatterns = [
          path('index/',views.index,name='index'),
          path('register/',views.register,name='register'),
          path('login/',views.user_login,name='login')
]




