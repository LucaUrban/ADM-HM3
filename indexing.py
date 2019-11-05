# importing lybraries
import nltk

# declarating global variables
rev_index_App = {}; rev_index = {}
commonWords = ["a", "an", "at", "and", "the", "by", "to", "i", "you", "he", "she", "it", "we", "they", "of", "is", "film", "in"
              , "with", "on", "up", "his", "her", "has", "him", "just", "all", "be", "but", "from", "or" , "are", "have", "has"
              , "into", "out", "still", "not"] # frequent words that hasn't meaning into the research of a movie

# does a first reverse indexing, at the end the result is represented by a dictionary with words as a key and the value
# associated is a list of integers where each integer represent the number of the page where the word compares. Ex:
# {"word_1": [1, 2, 4, 5], "word_2": [2, 5, 6] ...}
# so the word_a is into the first, second, fourth and fifth pages, the word_2 is into second, fifth and sixth page and so on
for i in range(1, 10001):
    # opening files and variables
    intro_plot = [] # the list that will contain the into and plot
    fileIn = open("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\film" + str(i) + ".tsv", encoding="utf-8")
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
        listaParole = nltk.word_tokenize(el); listaParoleAcc = []
        for j in range(len(listaParole)):
            if listaParole[j].isalpha() == True and listaParole[j].lower() not in commonWords:
                listaParoleAcc.append(listaParole[j].lower())
        for word in listaParoleAcc:
            if word not in rev_index.keys():
                rev_index_App[word] = [i]
            else:
                if i not in rev_index[word]:
                    rev_index_App[word].append(i)
    fileIn.close()

# this part creates a matrix with 2 columns and 10000 rows, each row contains the id of the word and the word associated
# Ex: [[1, word_1], [2, word_2], [3, word_3] ...]
dict_id = []
for i in range(len(rev_index_App.keys())):
    dict_id.append([i+1, list(rev_index_App.keys())[i]])

# this part creates a new dictionary where the keys aren't the words but their index
# Ex: {1: [1, 2, 3, 4], 2: [2, 4, 6, 7] ...}
for i in range(len(rev_index_App.keys())):
    values = list(rev_index_App.values())
    rev_index[dict_id[i][0]] = values[i]

# writes into two different files the matrix with the "conversion table" from an id to his word and the reverse index
# dictionary
fileIds = open("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\ids.txt", "w", encoding="utf-8")
fileIds.write(str(dict_id))
fileIds.close()
fileDict = open("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\reverseIndex.txt", "w", encoding="utf-8")
fileDict.write(str(rev_index))
fileDict.close()