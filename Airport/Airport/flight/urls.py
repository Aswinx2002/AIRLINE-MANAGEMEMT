
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import flight_list, flight_detail, add_flight, edit_flight, delete_flight, all_flights

urlpatterns = [

    path('account/add_flight/', add_flight, name='add_flight'),
    path('account/edit_flight/<slug:passed_flight_id>/', views.edit_flight, name='edit_flight'),
    path('account/delete_flight/<slug:passed_flight_id>/', delete_flight, name='delete_flight'),

    path('', views.home, name='home'),  # Home view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('flights/', views.flight_list, name='flight_list'),
    path('flight/<slug:passed_flight_id>/',flight_detail,name='flight_detail'),
    path('all_flights/', all_flights, name='all_flights'),
]
