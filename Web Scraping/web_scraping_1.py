#SIMPLE PYTHON PROGRAM TO EXTRACT SOME DATA FROM A TRAVEL SITE

import requests

from bs4 import BeautifulSoup

webpage = requests.get("https://www.expedia.com/things-to-do/stingray-sandbar-reef-sail.a177233.activity-details")

print(webpage.status_code)

#OUTPUT: 200

soup = BeautifulSoup(webpage.content, 'html.parser')

mainHeading = soup.find(class_="section-header-main")

print(mainHeading.prettify())

'''
OUTPUT:
<h1 class="section-header-main" id="activityTitle">
 Stingray Sandbar &amp; Reef Sail
</h1>
'''

print(mainHeading.get_text())

#OUTPUT: Stingray Sandbar & Reef Sail

costPerAdult = soup.find(id="activityFromPrice")

print(costPerAdult.get_text())

#OUTPUT: $85

subHeading = soup.find(class_="section-title").get_text()

print(subHeading)

#OUTPUT: Highlights

subHeadings = soup.find(id="highlights")

for i in subHeadings:
	print(i)

'''
OUTPUT:      
<li><p>Balmy &amp; clear turquoise waters ideal for snorkeling</p></li>
 
<li><p>Chance to swim with stingrays near a shallow sandbar</p></li>
 
<li><p>A tour of one of the Caymans' most-visited locations</p></li>
 
<li><p>Scenic cruise in a 65-foot (20 m) luxury catamaran</p></li>
 
<li><p>Close-up look at vibrant tropical fish in a natural setting</p></li>
'''
