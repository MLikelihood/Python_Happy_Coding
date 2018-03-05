# import requests
# from bs4 import BeautifulSoup
# #import beautifulsoup4
# url = 'http://github.com'
# r = requests.get(url)
# r_html = r.text
# soup = BeautifulSoup(r_html)
# title = soup.find('span', 'articletitle').string

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
       # print(story_heading.a.text)

    else:
        print(story_heading.contents[0].strip())
