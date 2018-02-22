import markovify
import tweepy

CONSUMER_KEY =""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#with open("pamTotal") as f:
#with open("michaelTotal") as f:
#with open("creedTotal") as f:
with open("dwightSchruteTotal") as f:
    text = f.read()

text_model = markovify.Text(text)

i = text_model.make_sentence()
while len(i) > 135 or len(i) < 80:
	i = text_model.make_sentence()

#i += " @rainnwilson"

api.update_status(i)

print("Tweeted: " + i)


