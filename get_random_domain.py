import random
import get_domains

class getRandomDomain(object):

    def __init__(self):

        with open("dictionary") as dict_file:
            word_list = dict_file.readlines()
        
        number_words = len(word_list)

        randomNum  = random.randint(0, number_words - 1)

        print word_list[randomNum]
        # test       = getDomains("hey")
        # listy      = test.queryAsk()

getRandomDomain()
