from bs4 import BeautifulSoup

# this function handles the response and extracts the links to the pages
def getLinks(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    film_list = soup.select("a")
    for i in range(len(film_list)):
        film_list[i] = film_list[i].get("href")
    return film_list