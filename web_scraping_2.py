#SIMPLE PROGRAM TO EXTRACT WEATHER FORECAST DATA OF A REGION

import requests

from bs4 import BeautifulSoup

webpage = requests.get("https://forecast.weather.gov/MapClick.php?textField1=37.78&textField2=-122.42#.WwCblZ-YW4E")

print(webpage.status_code)

#OUTPUT: 200

soup = BeautifulSoup(webpage.content, 'html.parser')

location = soup.find(class_="panel-title").get_text()

print(location)

#OUTPUT: SAN FRANCISCO DOWNTOWN (SFOC1)

forecast = soup.find(id="current_conditions-summary").get_text()

print(forecast)

'''
OUTPUT:

NA
58°F
14°C
'''
detailedForecast = soup.find(id="detailed-forecast").prettify()

print(detailedForecast)

'''
OUTPUT:

<div class="panel panel-default" id="detailed-forecast">
 <div class="panel-heading">
  <h2 class="panel-title">
   Detailed Forecast
  </h2>
 </div>
 <div class="panel-body" id="detailed-forecast-body">
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Tonight
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Increasing clouds, with a low around 53. Breezy, with a west wind 21 to 25 mph, with gusts as high as 32 mph.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Sunday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Cloudy, then gradually becoming mostly sunny, with a high near 61. Breezy, with a west wind 18 to 23 mph, with gusts as high as 30 mph.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Sunday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Increasing clouds, with a low around 52. Breezy, with a west wind 18 to 23 mph decreasing to 11 to 16 mph after midnight. Winds could gust as high as 30 mph.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Monday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Cloudy, then gradually becoming mostly sunny, with a high near 63. Breezy, with a west wind 7 to 12 mph increasing to 18 to 23 mph in the morning. Winds could gust as high as 30 mph.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Monday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly cloudy, with a low around 53. Breezy, with a west southwest wind 16 to 22 mph, with gusts as high as 29 mph.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Tuesday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Partly sunny, with a high near 63.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Tuesday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly cloudy, with a low around 54.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Wednesday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly sunny, with a high near 63.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Wednesday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Partly cloudy, with a low around 54.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Thursday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly sunny, with a high near 64.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Thursday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Partly cloudy, with a low around 53.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Friday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly sunny, with a high near 65.
   </div>
  </div>
  <div class="row row-odd row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Friday Night
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Partly cloudy, with a low around 53.
   </div>
  </div>
  <div class="row row-even row-forecast">
   <div class="col-sm-2 forecast-label">
    <b>
     Saturday
    </b>
   </div>
   <div class="col-sm-10 forecast-text">
    Mostly sunny, with a high near 62.
   </div>
  </div>
 </div>
</div>

'''

extendedForecast = soup.find_all(class_="tombstone-container")

tonight  = extendedForecast[0]

print(tonight.prettify())

'''
OUTPUT:

<div class="tombstone-container">
 <p class="period-name">
  Tonight
  <br/>
  <br/>
 </p>
 <p>
  <img alt="Tonight: Increasing clouds, with a low around 53. Breezy, with a west wind 21 to 25 mph, with gusts as high as 32 mph. " class="forecast-icon" src="DualImage.php?i=nwind_sct&amp;j=nbkn" title="Tonight: Increasing clouds, with a low around 53. Breezy, with a west wind 21 to 25 mph, with gusts as high as 32 mph. "/>
 </p>
 <p class="short-desc">
  Partly Cloudy
  <br/>
  and Breezy
  <br/>
  then Mostly
  <br/>
  Cloudy
 </p>
 <p class="temp temp-low">
  Low: 53 °F
 </p>
</div>
'''

print(tonight.get_text())

'''
OUTPUT:

Tonight
Partly Cloudyand Breezythen MostlyCloudyLow: 53 °F
'''

period_name = tonight.find(class_="period-name").get_text()

short_desc = tonight.find(class_="short-desc").get_text()

temp = tonight.find(class_="temp").get_text()

print(period_name)

#OUTPUT: Tonight

print(short_desc)

#OUTPUT: Partly Cloudyand Breezythen MostlyCloudy

print(temp)

#OUTPUT: Low: 53 °F

seven_day = soup.find(id="seven-day-forecast")

period_names = [x.get_text() for x in seven_day.select(".tombstone-container .period-name")]

short_descs = [y.get_text() for y in seven_day.select(".tombstone-container .short-desc")]

temps = [z.get_text() for z in seven_day.select(".tombstone-container .temp")]

import pandas as pd

thisWeekWeather = pd.DataFrame({"period-name": period_names, "short-desc": short_descs, "temp": temps})

print(thisWeekWeather)

'''
OUTPUT:
 
      period-name                                short-desc         temp
0         Tonight  Partly Cloudyand Breezythen MostlyCloudy   Low: 53 °F
1          Sunday                DecreasingClouds andBreezy  High: 61 °F
2     SundayNight  Partly Cloudyand Breezythen MostlyCloudy   Low: 52 °F
3          Monday                DecreasingClouds andBreezy  High: 63 °F
4     MondayNight  Partly Cloudyand Breezythen MostlyCloudy   Low: 53 °F
5         Tuesday                              Partly Sunny  High: 63 °F
6    TuesdayNight                             Mostly Cloudy   Low: 54 °F
7       Wednesday                              Mostly Sunny  High: 63 °F
8  WednesdayNight                             Partly Cloudy   Low: 54 °F
'''



