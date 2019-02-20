import requests
from bs4 import BeautifulSoup

season=str(input("Season: "))
episode=int(input("Episode: "))

url = "http://www.officequotes.net/no" + season + "-" + str(episode) + ".php"

if episode < 10:
	#If the episode is less than 10 there needs to be a leading 0
	url = "http://www.officequotes.net/no" + season + "-0" + str(episode) + ".php"

#print(url) for testing

r = requests.get(url)

nice = BeautifulSoup(r.text, "html.parser")

#open a file for the output
filename = "season" + season + "Episode" + str(episode)
f = open(filename, "w")
quotes = nice.find_all("div", {"class": "quote"})

if quotes:
	for quote in quotes:
		f.write(quote.text)
		print(quote.text)

	print("\n\nOUTPUT PRINTED TO",filename)
	f.close()

else:
	print("\nEpisode not found or connection fail\n")
