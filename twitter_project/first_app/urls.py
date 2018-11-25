from django.urls import path
from . import views


app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('last_tweets/', views.latest_tweets, name='last_tweets' ),
	path('signup/', views.signup, name='signup'),
	path('user_profile/<int:user_id>', views.user_profile, name='user_profile'),
	path('write_a_new_tweet/', views.form_new_tweet, name='new_tweet'),
	path('write_a_new_tweet/<int:user_id>', views.new_user_tweet, name='new_tweet'),
]