from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Game_of_Thrones"

response = urlopen(url).read()

soup = BeautifulSoup(response, "lxml")
views = []
total = 0.0
for links in soup.find("table", attrs={"class":"wikitable plainrowheaders"}).findAll("th", attrs={"scope":"row"}):
    for link in links.findAll("a"):
        season_url =  "https://en.wikipedia.org" + link["href"]
        season_html = urlopen(season_url).read()
        season_soup = BeautifulSoup(season_html, "lxml")

        rows = season_soup.find("table", attrs={"class":"wikitable plainrowheaders wikiepisodetable"}).findAll("tr", attrs={"class": "vevent"})
        for row in rows:
            view = row.findAll("td")[-1].find(text = True)
            if view != "TBD":
                views.append(view)
                total +=float(view)

print("Skupno stevilo vseh gledalcev serije Game of Thrones,\n" +
" ki so si posamezno epizodo pogledali prvi dan predvajanja je: %.2f  milijonov." % total)
