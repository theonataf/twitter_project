from django import forms
from django.core import validators
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

class NewUserTweetForm(forms.Form):
	text = forms.CharField(max_length=140, widget=forms.Textarea)
	

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')
	
class UserLoginForm(forms.Form):
    
    username= forms.CharField(max_length= 150)
    password= forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        all_clean_data= super().clean()
        return all_clean_data