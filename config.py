import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
API_KEY_SECRET = os.environ.get('API_KEY_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)