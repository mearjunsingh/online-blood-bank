from django.urls import path
from .views import (
    cancel_request_status,
    complete_request_status,
    deny_request_status,
    home_page,
    offer_help,
    pending_requests,
    search_page,
    submit_request,
    user_page,
    verify_request_status
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('search/', search_page, name='search_page'),
    path('user/<int:id>/', user_page, name='user_page'),
    path('submit-request/', submit_request, name='submit_request'),
    path('pending-requests/', pending_requests, name='pending_requests'),
    path('offer-help/<int:id>/', offer_help, name='offer_help'),
    path('verify-request-status/<int:id>/', verify_request_status, name='verify_request_status'),
    path('complete-request-status/<int:id>/', complete_request_status, name='complete_request_status'),
    path('cancel-request-status/<int:id>/', cancel_request_status, name='cancel_request_status'),
    path('deny-request-status/<int:id>/', deny_request_status, name='deny_request_status')
]