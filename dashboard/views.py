from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


from .models import Bitcoin, Paypal, Transaction, HubRequest

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        invests2 = Transaction.objects.filter(user=request.user)
        invests = invests2.order_by('sn')
        context = {
        'invests': invests
        }

        print(invests)

        return render(request, 'dashboard.html', context)
    else:
        return redirect('signin')

def deposit(request):
    if request.user.is_authenticated:
        return render(request, 'deposit.html')
    else:
        return redirect('signin')

def payment(request):
    if request.user.is_authenticated:
        return render(request, 'payment.html')
    else:
        return redirect('signin')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('signin')

def hubtrade(request):
    if request.user.is_authenticated:
        return render(request, 'hubtrade.html')
    else:
        return redirect('signin')

def tradedetails(request):
    if request.user.is_authenticated:
        return render(request, 'tradedetails.html')
    else:
        return redirect('signin')

def fusionform(request):
    if hasattr(request.user, 'hubrequest'):
        return render(request, 'hubtrade.html')

    else:
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phone = request.POST['phone']
            country = request.POST['country']
            state = request.POST['state']
            job = request.POST['job']
            income = request.POST['income']
            marital = request.POST['marital']
            bio = request.POST['bio']

            hubrequest = HubRequest(firstname=firstname, lastname=lastname, email=email, bio=bio, phone=phone, country=country, state=state, job=job, income= income, marital=marital)

            hubrequest.user = request.user
            hubrequest.save()
            
            return redirect('tradedetails')
            

def hub(request):
    if hasattr(request.user, 'fusion'):
        return render(request, 'hub.html')

    else: 
        return render(request, 'fusionform.html')


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
                
                # subject = "Welcome to FX Pro Investment"
                # message = f'Hello {username}, thank you for signing up to our platform'
                # from_email = settings.EMAIL_HOST_USER
                # to = [username]

                # html_message = render_to_string('email.html', {'first_name': first_name})
                # message = EmailMessage(subject, html_message, from_email, [to])
                # message.content_subtype = 'html'
                # message.send()

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
            
            messages.success(request, 'Withdrawal Processing, You\'ll receive an  Email Shortly')
            return render(request, 'withdraw.html')

    else:
        return redirect('signin')
