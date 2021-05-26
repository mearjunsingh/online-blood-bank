from django.urls import path
from .views import (
    changePassword_page,
    dashboard_page,
    login_page,
    logout_page,
    manage_request_page,
    register_page
)
from .ajax_views import (
    change_is_donor
)


urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('dashboard/manage-requests/', manage_request_page, name='manage_request_page'),
    path('dashboard/change-password/', changePassword_page, name='changePassword_page'),
    path('dashboard/logout/', logout_page, name='logout_page'),
    # AJAX URLS
    path('ajax/change_is_donor/', change_is_donor, name='change_is_donor_page')
]
