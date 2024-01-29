from lemmatizer import *

def test():
    testWords = ['Nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai', 'truovato']
    testLemmatizer = Lemmatizer(testWords)
    testLemmatizerResult = testLemmatizer.lemmatize()
    return testLemmatizerResult
