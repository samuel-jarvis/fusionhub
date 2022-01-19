from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        # country = request.POST['country']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message, phone=phone)

        contact.save()
        # return redirect('contacts')

    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')


def deposit(request):
    if request.user.is_authenticated:
        return render(request, 'deposit.html')
    else:
        return redirect('login')

def fusionhub(request):
    return render(request, 'fusionhub.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
				# messages.success(request, 'You are now logged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('signin')
        else:
            return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
			#Check email
            if User.objects.filter(username=username).exists():
                messages.error(request, 'It seems you are already registered signin')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                
                subject = "Welcome to FX Pro Investment"
                message = f'Hello {username}, thank you for signing up to our platform'
                from_email = settings.EMAIL_HOST_USER
                to = [username]

                html_message = render_to_string('email.html', {'first_name': first_name})
                message = EmailMessage(subject, html_message, from_email, [to])
                message.content_subtype = 'html'
                message.send()

                # send_email(subject, email_from, ['to',] , html_message = html_message)

                messages.success(request, 'You are now registered and can log in')
                return redirect('signin')
        else:
            messages.error(request, "Passwords do not Match")
            return redirect ('signup')
    else:
        return render(request, 'signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect ('signin')

def withdraw(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'withdraw.html')


        if request.method == 'POST' and 'bitcoin' in request.POST:
            amount = request.POST['amount']
            wallet = request.POST['wallet']
            username = request.POST['username']

            withdraw = Bitcoin(amount=amount, wallet=wallet, username=username)

            withdraw.save()

            messages.success(request, 'Withdrawal Processing')
            return render(request, 'withdraw.html')

        if request.method == 'POST' and 'paypal' in request.POST:
            amount = request.POST['amount']
            email = request.POST['email']
            username = request.POST['username']

            withdraw = Paypal(amount=amount, email=email, username=username)

            withdraw.save()
            
            messages.success(request, 'Withdrawal Processing')
            return render(request, 'withdraw.html')

        if request.method == 'POST' and 'bank' in request.POST:
            amount = request.POST['amount']
            account_name = request.POST['accountname']
            bank_name = request.POST['bankname']
            account_number = request.POST['accountnumber']
            username = request.POST['username']


            withdraw = Bank(amount=amount, account_name=account_name, bank_name=bank_name, account_number=account_number, username=username)

            withdraw.save()

            messages.success(request, 'Withdrawal Processing')
            return render(request, 'withdraw.html')

    else:
        return redirect('login')
