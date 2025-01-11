# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *
from geopy.distance import geodesic
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return redirect('card_details')
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('card_details')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, age=form.cleaned_data['age'],phone_number=form.cleaned_data['phone_number'])
            RFIDCard.objects.create(user=user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def card_details(request):
    card = RFIDCard.objects.get(user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = RechargeForm(request.POST)
        if form.is_valid():
            card.balance += form.cleaned_data['amount']
            card.save()
            return redirect('card_details')
    else:
        form = RechargeForm()
    return render(request, 'card_details.html', {'card': card, 'profile': profile, 'form': form})





def process_rfid_transaction(request):
    if request.method=="POST":
        form=TransactionForm(request.POST)

        if form.is_valid():
            transaction=form.save(commit=False)

            amount_to_be_deducted=transaction.calculate_amount()

            rfid_card=transaction.rfid_card
            if rfid_card.balance>=amount_to_be_deducted:
                rfid_card.balance-=Decimal(amount_to_be_deducted)
                rfid_card.save()

                transaction.save()

                return redirect('transaction-success')
            else:
                return render(request,'insufficient_balance.html')
    else:
        form=TransactionForm()

    return render(request,'process_transaction.html',{'form':form})
def transaction_success(request):
    return render(request,'transaction_success.html')



@login_required
def transaction_history(request):
    transactions=RFIDCardLog.objects.filter(user=request.user)
    return render(request,'transaction_history.html',{'transactions':transactions})
