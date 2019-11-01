import collector_utils
import requests

# doing the request to the web page with the films
request = requests.get("https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html")
film_links = collector_utils.getLinks(request)

# extract the pages from wikipedia site
for i in range(len(film_links)):
    url_file = "C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\HM3\\article_" + str(i+1) + ".html"
    file = open(url_file, "w", encoding="utf-8")
    file.write(str(requests.get(film_links[i]).text))

