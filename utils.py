import nltk; from nltk.corpus import stopwords
from bs4 import BeautifulSoup

# this function handles the response and extracts the links to the pages
def getLinks(request):
    soup = BeautifulSoup(request.text, 'html.parser')
    film_list = soup.select("a")
    for i in range(len(film_list)):
        film_list[i] = film_list[i].get("href")
    return film_list

def parser(film, fileOut):
    # inizializing variables
    flag = 0; director = "NA"; producer = "NA"; writer = "NA"; starring = "NA"; music = "NA"; release_date = "NA";
    runtime = "NA"; country = "NA"; language = "NA"; budget = "NA"

    # extract title of the page and the film
    list_h1 = film.select("h1")
    for h1 in list_h1:
        if h1.get("id") == "firstHeading":
            fTitle = h1.text

    # this part trys to extract the intro and plot of the film, if they aren't into the page they are set to NA
    try:
        intro = film.select("p")[0].text
        plot = film.select("p")[1].text
    except:
        intro = "NA";
        plot = "NA"
    finally:

        # search and then extract the required values from the infobox table related to the film
        fTables = film.select("table")
        for table in fTables:
            if table.get("class") != None:
                if "infobox" in table.get("class"):
                    rows = table.select("tr")
                    for row in rows:
                        for el in row.select("th"):
                            if "class" in el.attrs.keys():
                                if "summary" in el.attrs["class"]:
                                    flag = 1
                                    summary = el.text
                                else:
                                    summary = "NA"
                            if el.text == "Directed by":
                                director = row.select("td")[pos].text
                            if el.text == "Produced by":
                                producer = row.select("td")[pos].text
                            if el.text == "Written by":
                                writer = row.select("td")[pos].text
                            if el.text == "Starring":
                                starring = row.select("td")[pos].text
                            if el.text == "Music by":
                                music = row.select("td")[pos].text
                            if el.text == "Release date":
                                release_date = row.select("td")[pos].text
                            if el.text == "Running time":
                                runtime = row.select("td")[pos].text
                            if el.text == "Country":
                                country = row.select("td")[pos].text
                            if el.text == "Language":
                                language = row.select("td")[pos].text
                            if el.text == "Budget":
                                budget = row.select("td")[pos].text
                            pos += 1
                        pos = 0

        # write into the result file all the important data extracted according to the format of a tsv file
        if flag == 0: summary = "NA"
        fileOut.write(
            fTitle + " \t " + intro + " \t " + plot + " \t " + summary + " \t " + director + " \t " + producer + " \t " +
            writer + " \t " + starring + " \t " + music + " \t " + release_date + " \t " + runtime + " \t " + country +
            " \t " + language + " \t " + budget)

def firstRevIndexing():
    rev_index_App = {}; commonWords = set(stopwords.words("english"))
    for i in range(1, 10001):
        # opening files and variables
        fileIn = open("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\film" + str(i) + ".tsv", encoding="utf-8")
        intro_plot = []
        fileText = fileIn.read()

        # extract the summary, intro and the plot of each film article
        for j in range(3):
            intro_plot.append(fileText[:fileText.find("\t")].strip())
            fileText = fileText[fileText.find("\t") + 2:]

        # first removes the summary because it isn't required for the indexing of the words
        # then does a parsing of the string represented by the el variable transforming it into a list of words then
        # controls if the word is "legit" and insert it into a list that will be used after to construct a first result
        # dictionary as exposed into the comment that begins on the row 10
        intro_plot.pop(0)
        for el in intro_plot:
            listaParole = nltk.word_tokenize(el);
            listaParoleAcc = []
            for j in range(len(listaParole)):
                if listaParole[j].isalpha() == True and listaParole[j].lower() not in commonWords:
                    listaParoleAcc.append(listaParole[j].lower())
            for word in listaParoleAcc:
                if word not in rev_index_App.keys():
                    rev_index_App[word] = [i]
                else:
                    if i not in rev_index_App[word]:
                        rev_index_App[word].append(i)
        fileIn.close()
        return rev_index_App

def listId(dic):
    dict_id = []
    for i in range(len(dic.keys())):
        dict_id.append([i + 1, list(dic.keys())[i]])
    return dict_id

def revIndex(dic):
    reverseIn = {}
    for i in range(len(dic.keys())):
        reverseIn[i + 1] = list(dic.values())[i]
    return reverseIn

def fileWrite(path, ogg):
    fileIds = open(path, "w", encoding="utf-8")
    fileIds.write(str(ogg))