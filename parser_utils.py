# importing libraries
from bs4 import BeautifulSoup

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

