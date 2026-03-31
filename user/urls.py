# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login, name='login'),
#     path('register/', views.register, name='register'),
#     path('profile/', views.profile, name='profile'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]