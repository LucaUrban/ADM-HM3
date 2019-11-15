# importing lybraries
import indexing_utils

# does a first reverse indexing, at the end the result is represented by a dictionary with words as a key and the value
# associated is a list of integers where each integer represent the number of the page where the word compares. Ex:
# {"word_1": [1, 2, 4, 5], "word_2": [2, 5, 6] ...}
# so the word_a is into the first, second, fourth and fifth pages, the word_2 is into second, fifth and sixth page and
# so on
rev_index_App = indexing_utils.firstRevIndexing()

# this part creates a matrix with 2 columns and 10000 rows, each row contains the id of the word and the word associated
# Ex: [[1, word_1], [2, word_2], [3, word_3] ...]
dict_id = indexing_utils.listId(rev_index_App)

# this part creates a new dictionary where the keys aren't the words but their index
# Ex: {1: [1, 2, 3, 4], 2: [2, 4, 6, 7] ...}
rev_index = indexing_utils.revIndex(rev_index_App)

# writes into two different files the matrix with the "conversion table" from an id to his word and the reverse index
# dictionary
indexing_utils.fileWrite("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\vocabulary.txt", dict_id)
indexing_utils.fileWrite("C:\\Users\\asus\\Desktop\\Algoritmic methods for data science\\ADM-HM3\\articles\\reverseIndex.txt", rev_index)