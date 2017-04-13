import random

class getRandomQuery(object):

    def __init__(self):
        pass

    def randomQueryTerms(self):

        with open("dictionary") as dict_file:
            word_list = dict_file.readlines()

        words_len = len(word_list)
        query_list = []
        query     = str()

        for number in range(4):
            randomNum  = random.randint(0, words_len - 1)
            query_list.append(word_list[randomNum])

        for word in query_list:
            if query_list.index(word) != 0:
                query += word
            else:
                query += word
        return query