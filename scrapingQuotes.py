import requests
from bs4 import BeautifulSoup

season = "8"
#episode = raw_input("Episode: ")
for i in range(2, 3):
	url = "http://www.officequotes.net/no" + season +"-" + str(i) + ".php"

	if i < 10:
		#print("It was less than 10")
		url = "http://www.officequotes.net/no" + season +"-0" + str(i) + ".php"

	#print(url)

	r = requests.get(url)

	nice = BeautifulSoup(r.content, "lxml")
	f = open("episodes/s" + season + "e" + str(i), "w")
	for x in nice.find_all("div", {"class": "quote"}):
		f.write(x.text.encode('utf8'))

	f.write("\nTHIS IS THE END OF THE SCRIPT")

	f.close()
