from django.shortcuts import render
from .models import donations

# Create your views here.

def donate1(request):
    if request.method == 'POST':
        don = donations()
        don.firstname = request.POST.get('first_name')
        don.lastname = request.POST.get('last_name')
        don.email = request.POST.get('email_id')
        don.phone = request.POST.get('phone_number')
        don.firstname = request.POST.get('first_name')
        don.contribution_type = request.POST.get('contribution_type')
        don.amount = request.POST.get('value')
        don.save()
        return render(request, 'about.html', {})
    else:
        return render(request, 'about.html', {})
