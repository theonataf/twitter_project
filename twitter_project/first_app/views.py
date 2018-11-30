from django.shortcuts import render, redirect
from first_app.models import Tweet, UserProfileInfo
from django.contrib.auth.models import User
from django.http import HttpResponse
from first_app.forms import NewUserTweetForm, UserForm, UserProfileInfoForm, UserLoginForm
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.

def index(request):
	last_tweets = {
	'tweet' : Tweet.objects.all().order_by('-date')[:20],
	}
	return render(request, 'index.html', context=last_tweets)

def signup(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.seword(useword)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profil.profile_pic = request.FILES['profile_pic']

			profile.save()
			registered = True
		
		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'signup.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
		})

		
'''def loging_view(request):
	
	login_form = forms.LoginForm(data=request.POST)
	if request.method == 'POST':
		login_form = forms.LoginForm(data=request.POST)
		loging(request, login_form['username'], login_form['password'])
	return render(request, 'login.html', context={'login_form': login_form})'''

def log_in(request):
	log_in_done = False
	if request.method =='POST':
		user_login_form = UserLoginForm(data= request.POST)
		if user_login_form.is_valid():
			clean_data=user_login_form.clean()

			username = clean_data['username']
			password = clean_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				print('ok le user est log in ' )
				return HttpResponse('The user is login mofo {}'.format(user.id))
			else:
				return HttpResponse('This user does not exist')

	else:
		user_login_form = UserLoginForm()
		return render(request, 'login.html', context= {
			'form' : user_login_form
			})

@login_required
def logout_view(request):
	logout(request)
	user_login_form = UserLoginForm()
	return redirect('/first_app/login/')

@login_required
def profile(request, user_id):
	is_logged = False
	if not request.user.is_authenticated:
		return render(request, 'permission_error.html')
	
	else:
		user = User.objects.get(id=user_id)
		if request.user.id == user_id:
			is_logged = True
		return render(request,'profile.html', context={
			'tweet': gets_all_tweets_of_user(user_id)['tweet'], 
			'is_logged': is_logged })



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })




def latest_tweets(request):
	last_tweets = {
	 'tweet' : Tweet.objects.all().order_by('-date')[:20],
	 }
	return render(request, 'last_tweets.html', context=last_tweets)


def gets_all_tweets_of_user(user_id):
  
	all_tweets = {
	'tweet' : Tweet.objects.filter(user= user_id).order_by('-date')[:20],
	}
	return all_tweets


def user_profile(request, user_id):
	return render(request, 'user_profile.html', context=gets_all_tweets_of_user(user_id))


def form_new_tweet(request):
	form = NewTweetForm()
	if request.method == 'POST':
		form = NewTweetForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error - form is unvalid')

	return render(request, 'write_a_new_tweet.html', {'form': form})


def new_user_tweet(request, user_id):
	user = User.objects.get(id=user_id)
	form = NewUserTweetForm()
	if request.method == 'POST':
		form = NewUserTweetForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			tweet = Tweet(text=text, user=user, date=datetime.datetime.now())
			tweet.save()
			return redirect('/first_app/last_tweets')
		else:
			print('Error - form is unvalid')

	return render(request, 'write_a_new_tweet.html', context={'form': form, 'user': user})














