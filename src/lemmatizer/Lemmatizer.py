# pip install spacy
# python -m spacy download it_core_news_sm

import treetaggerwrapper
import spacy 

class TreeTaggerLemmatizer:
    '''Lemmatizer is able to perform the lemmatization of words provided'''

    def __init__(self, wordlist):
        '''Create a new instance of Lemmatizer'''
        ''' wordlist:  -- (List of strings) List of words to be lemmatized'''

        self.wordlist = wordlist
        self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
 
    def lemmatize(self):
        '''Lemmatize words in wordlist of Lemmatizer
        returns:  -- (List of strings) List of lemmatized words'''

        tags = self.tagger.tag_text(self.wordlist)
        lemmas = [tag.split('\t')[2] for tag in tags]
        return lemmas
    

class SpaCyLemmatizer:
    def __init__(self, wordlist, language="it_core_news_sm"):
        self.wordlist = wordlist
        self.nlp = spacy.load(language)

    def lemmatize(self):
        doc = self.nlp(" ".join(self.wordlist))
        lemmas = [token.lemma_ for token in doc]
        return lemmas


# Test
# testWords = ['Nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita']

# # Ausgabe
# testLemmatizer = TreeTaggerLemmatizer(testWords)
# testLemmatizerResult = testLemmatizer.lemmatize()
# print("\nTreeTagger >>", testLemmatizerResult)

# testLemmatizer2 = SpaCyLemmatizer(testWords)
# testLemmatizerResult2 = testLemmatizer2.lemmatize()
# print("SpaCy >>", testLemmatizerResult2)