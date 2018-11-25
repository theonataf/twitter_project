from django.shortcuts import render, redirect
from first_app.models import Tweet, UserProfileInfo
from django.contrib.auth.models import User
from . import forms
import datetime


# Create your views here.

def index(request):
	last_tweets = {
	'tweet' : Tweet.objects.all().order_by('-date')[:20],
	}
	return render(request, 'index.html', context=last_tweets)

def signup(request):
	registered = False

	if request.method == 'POST':
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)

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
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()

	return render(request, 'signup.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
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
	form = forms.NewTweetForm()
	if request.method == 'POST':
		form = forms.NewTweetForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error - form is unvalid')

	return render(request, 'write_a_new_tweet.html', {'form': form})


def new_user_tweet(request, user_id):
	user = User.objects.get(id=user_id)
	form = forms.NewUserTweetForm()
	if request.method == 'POST':
		form = forms.NewUserTweetForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			tweet = Tweet(text=text, user=user, date=datetime.datetime.now())
			tweet.save()
			return redirect('/first_app/last_tweets')
		else:
			print('Error - form is unvalid')

	return render(request, 'write_a_new_tweet.html', context={'form': form, 'user': user})












