import nltk; from nltk.corpus import stopwords

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