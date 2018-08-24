import markovify
import tweepy
import sys

CONSUMER_KEY =""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

args = len(sys.argv)

if args == 1:
    #this is default situation (no params)
    with open("dwightSchruteTotal") as f:
        text = f.read()

if args == 2:
    value = sys.argv[1]
    value = value.lower()

    if value == "dwight":
        with open("dwightSchruteTotal") as f:
            text = f.read()

    elif value == "creed":
        with open("creedTotal") as f:
            text = f.read()


text_model = markovify.Text(text)

i = text_model.make_sentence()
while len(i) > 135 or len(i) < 80:
	i = text_model.make_sentence()

#i += " @rainnwilson"

api.update_status(i)

print("Tweeted: " + i)


