import treetaggerwrapper

class Lemmatizer:
    '''Lemmatizer is able to perform the lemmatization of words provided'''

    def __init__(self, wordlist):
        '''Create a new instance of Lemmatizer'''
        ''' wordlist:  -- (List of strings) List of words to be lemmatized'''
        self.wordlist = wordlist
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')

        
    def lemmatize(self):
        '''Lemmatize words in wordlist of Lemmatizer
        returns:  -- (List of strings) List of lemmatized words'''

        #tags = self.tagger.tag_text(" ".join(self.wordlist))
        tags = self.tagger.tag_text(self.wordlist)
        print(tags) 
        lemmas = [tag.split('\t')[2] for tag in tags]
        print(lemmas)

        return lemmas
    
    
# test
testWords = ['Nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita']
testLemmatizer = Lemmatizer(testWords)
testLemmatizerResult = testLemmatizer.lemmatize()