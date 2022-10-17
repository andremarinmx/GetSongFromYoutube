from bs4 import BeautifulSoup
import requests

#Put the url about your playlist
url = 'https://www.youtube.com/playlist?list=PLNYeagcf77NqE9w2hYJ997UABaDS1L_ge'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#$x('//div/h3/a/text()').map(x=>x.wholeText)