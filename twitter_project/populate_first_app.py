import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_project.settings')
import django
django.setup()


# Fake populate script
from faker import Faker 
from first_app.models import UserProfileInfo, Tweet
from django.contrib.auth.models import User

fakegen = Faker()

def populate(N=5):
	for entry in range(N):
		
		# create fake data for the entry
		user_fake_username  = fakegen.user_name() 
		user_fake_first_name = fakegen.first_name()
		user_fake_last_name = fakegen.last_name()
		user_fake_password = fakegen.password()
		user_fake_bio = fakegen.text()
		

		#create the fake webpage entry
		user = User.objects.get_or_create(username=user_fake_username, 
			first_name=user_fake_first_name,last_name=user_fake_last_name, password=user_fake_password)[0]
		userprofileinfo = UserProfileInfo.objects.get_or_create(user=user, bio=user_fake_bio)   

		#create the fake access record entry
		for entry in range(20):
			tweet_fake_date = fakegen.date()
			tweet_fake_tweet = fakegen.text()
			tweet = Tweet.objects.get_or_create(text=tweet_fake_tweet, 
				date=tweet_fake_date, user=user)[0]


if __name__ == '__main__':
	print('Staring to populate...')
	populate(120)
	print('Finished populating!')


