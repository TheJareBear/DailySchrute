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
	with open("dwightTotal") as f:
		text = f.read()

if args == 2:
	value = sys.argv[1]
	value = value.lower()

	if value == "dwight":
		with open("dwightTotal") as f:
		  text = f.read()

	if value == "creed":
		with open("creedTotal") as f:
		  text = f.read()

	if value == "pam":
		with open("pamTotal") as f:
			text = f.read()

	if value == "michael":
		with open("michaelTotal") as f:
			text = f.read()

	if value == "total":
		with open("allCharactersTotal") as f:
			text = f.read()


text_model = markovify.Text(text)

msg = ""

try:
	while len(msg) > 230 or len(msg) < 80:
		msg = text_model.make_sentence()
		while msg is None:
			msg = text_model.make_sentence()

	api.update_status(msg)

	print("Tweeted: " + msg)

except:
	print("Model Failed")



