from django.contrib import admin
from django.urls import path
from .views import (
    dashboard_page,
    home_page,
    login_page,
    register_page,
    search_page,
    user_page,
)
from .ajax_views import (
    change_is_donor
)


urlpatterns = [
    path('', home_page, name='home_page'),
    path('search/', search_page, name='search_page'),
    path('user/', user_page, name='user_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    # AJAX URLS
    path('ajax/change_is_donor/', change_is_donor, name='change_is_donor_page')
]
