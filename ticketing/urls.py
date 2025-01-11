# myapp/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('card-details/', card_details, name='card_details'),
    path('process_transaction/',process_rfid_transaction,name='process_transaction'),
    path('transaction-success/',transaction_success,name='transaction-success'),
    path('transaction_history/',transaction_history,name='transaction_history')
]
