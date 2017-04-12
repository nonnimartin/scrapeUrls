import get_random_query as query

class getUrls(object):

    def ranUrl(self):

        random_query_obj = query.getRandomDomain()
        random_word      = random_query_obj.randomDomain()
        return random_word

test = getUrls()

print test.ranUrl()