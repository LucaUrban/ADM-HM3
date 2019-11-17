# importing libraries
from bs4 import BeautifulSoup
import  parser_utils

# extracting data from crawled HTML pages and transform it into a film.tsv file with the extracted informations as specified
# into the requests
for i in range(10000):
    # creating url, open file and parsing it
    url = "C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\article_" + str(i + 1) + ".html"
    fileIn = open(url, "r", encoding="utf-8")
    fileOut = open("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\film" + str(i + 1) + ".tsv", "a", encoding="utf-8")
    film = BeautifulSoup(fileIn.read(), "html.parser")

    # extract tre needed information about the film and write it into the fileOut
    parser_utils.parser(film, fileOut)

    # close the files that aren't used
    fileIn.close(); fileOut.close()