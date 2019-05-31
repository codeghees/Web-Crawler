
# importing the requests library 
# taken help from https://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup

import requests 
from bs4 import BeautifulSoup

global redlist
redlist = []
def directorydots(parenturl, nextURL):
	print("directorydots")
	print (nextURL)
		
def crawler(url,base,visited):
	r = requests.get(url) 
	if r.status_code != 200:
		return
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	for link in soup.find_all('a'):
		nextURL = link.get('href')
		# print("nextURL = ",nextURL)
		newURL = ''

		if (nextURL != "") and (nextURL!="#") and (nextURL!= None) and ("mailto" not in nextURL ) and ("javascript" not in nextURL) and ("irc" not in nextURL):

			if base in nextURL: # if nextURl already a full URL, for recursion
				newURL = nextURL
			if nextURL[0] == "/":
				newURL = base[0:-1] + nextURL
			if nextURL[0] == ".":
				directorydots(url,nextURL)
				continue
			if "http" != nextURL[0:4]:
				newURL = base + nextURL
			if newURL not in visited and newURL != '':
				visited.append(newURL)
				print(newURL)
				crawler(newURL,base,visited)
	return visited
			

def main():
	# URL = "https://www.syedfaaizhussain.com/"
	# URL = "http://www.learnyouahaskell.com/"
	# URL = "http://www.carameltechstudios.com/"
	URL = input("Enter a URL inclusive of all http or https tags\n")
	counter = 0
	redlist.append(URL)
	sites= crawler(URL,URL,redlist)
	print(len(sites))

main()