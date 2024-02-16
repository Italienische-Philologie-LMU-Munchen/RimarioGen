class RhymeWordProcessor:
    '''RhymeWordProcessor is able to further process a list of rhyme words: It can manipulate the list or perform several calculations
    '''

    def __init__(self, rhymeWords):
        '''Create a new instance of RhymeWordProcessor

        rhymeWords:  -- (List of strings) List of rhyme words to be processed'''
        self.rhymeWords = rhymeWords

    def getRhymeWordMethodNames(self):
        '''Get all method names that are associated with the analysis/manipulation of rhyme word list

        returns:  -- (List of strings) List of all method names associated with analysis/manipulation of rhyme word list'''
        rhymeWordMethods = [func for func in dir(RhymeWordProcessor) if (callable(getattr(
            RhymeWordProcessor, func)) and func.startswith("rhymeWords"))]
        return rhymeWordMethods

    def setRhymeWords(self, rhymeWords):
        '''Set internal rhyme word list of RhymeWordProcessor

        rhymeWords:  -- (List of strings) List of rhyme words to be processed'''
        self.rhymeWords = rhymeWords

    def hasRhymeWords(self):
        '''Get information whether there is an internal rhyme word list with rhyme words

        returns:  -- (Boolean) Value indicating whether there are ryhme words in internal rhyme word list or not'''
        return (self.rhymeWords == None or len(self.rhymeWords) == 0)

    def rhymeWordsRemoveDuplicates(self):
        '''Remove duplicates of internal rhyme word list
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List if strings) List of rhyme words wihtout duplicates'''
        # statt der Standardmethode set() zum Entfernen von Duplikaten wird hier in ein dictionary umgewandelt, da so die Wörter in der Reihenfolge ihres Erscheinens bleiben

        rhymeword_dict = dict.fromkeys(self.rhymeWords)
        rhymewords_withoutDuplicates = list(rhymeword_dict)
        return rhymewords_withoutDuplicates

    def rhymeWordsGetRawList(self):
        '''Deliver internal rhyme word list without any modifications/calculations

        returns:  -- (List of strings) List of rhyme words (internal unmodificated list)'''
        return self.rhymeWords

    def TBDrhymeWordsSortByOccurences(self):
        '''Deliver rhyme word list sorted by the number of occurences, so the most frequent rhyme word will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by occurrences'''
        # TBD
        # Veronika
        occurences = []
        for word in self.rhymeWords:
            occurence = self.rhymeWords.count(word)
            occurences.append(occurence)
        # sort_order = sorted(occurences)
        # sorted(self.rhymeWords, key = lambda i: sort_order.index(i[0]))

        print("RhymeWordProcessor hasn't been implemented yet.")

    def rhymeWordsSortByLength(self):
        '''Deliver rhyme word list sorted by the length of the words, so the rhyme word with most letters will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by length'''

        rhymewordsByLength = sorted(self.rhymeWords, key=len)
        return rhymewordsByLength

    def rhymeWordsSortAlphabetically(self):
        '''Deliver rhyme word list sorted alphabetically, so the rhyme word starting with an "A" will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted alphabetically'''
        rhymewordsAlphabetically = sorted(self.rhymeWords)
        return rhymewordsAlphabetically

    def rhymeWordsSortAlphabeticallyLastLetter(self):
        '''Deliver rhyme word list sorted alphabetically considering the last letter, so the rhyme word ending with an "A" will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted alphabetically considering their last letter'''
        def sortByLastLetter(s):
            return s[-1], s
        rhymewordsAlphabeticallyReverse = sorted(
            self.rhymeWords, key=sortByLastLetter)
        return rhymewordsAlphabeticallyReverse

    def rhymeWordsSortByNumberOfVowels(self):
        '''Deliver rhyme word list sorted by the number of vowels, so the rhyme word containing the highest number of vowels will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by their number of vowels'''
        def sortByNumberOfVowels(string):
            count = 0
            for letter in string:
                if letter in ['a', 'á', 'à', 'â', 'ä', 'A', 'Á', 'À', 'Â', 'Ä',
                              'e', 'é', 'è', 'ê', 'ë', 'E', 'É', 'È', 'Ê', 'Ë',
                              'i', 'í', 'ì', 'î', 'ï', 'I', 'Í', 'Ì', 'Î', 'Ï',
                              'o', 'ó', 'ò', 'ô', 'ö', 'O', 'Ó', 'Ò', 'Ô', 'Ö',
                              'u', 'ú', 'ù', 'û', 'ü', 'U', 'Ú', 'Ù', 'Û', 'Ü'
                              ]:
                    count = count+1
            return count

        rhymwordsByNumberOfVowels = sorted(
            self.rhymeWords, key=sortByNumberOfVowels)
        return rhymwordsByNumberOfVowels

    def TBDrhymeWordsSortByVowelFrequency(self):
        '''Deliver rhyme word list sorted by their vowel frequency, so the rhyme word containing the highest relative number of vowels (vowels out of all letters of word) will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by vowel frequency'''
        # TBD
        print("RhymeWordProcessor hasn't been implemented yet.")

    def rhymeWordsSortByNumberOfConsonants(self):
        '''Deliver rhyme word list sorted by the number of consonants, so the rhyme word containing the highest number of consonants will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by their number of consonants'''
        def sortByNumberOfConsonants(string):
            count = 0
            for letter in string:
                if letter in ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', 'j', 'J', 'ç', 'Ç', 'ſ'
                              ]:
                    count = count+1
            return count

        rhymwordsByNumberOfConsonants = sorted(
            self.rhymeWords, key=sortByNumberOfConsonants)
        return rhymwordsByNumberOfConsonants

    def TBDrhymeWordsSortByConsonantFrequency(self):
        '''Deliver rhyme word list sorted by their consonant frequency, so the rhyme word containing the highest relative number of consonants (consonants out of all letters of word) will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by vowel frequency'''
        # TBD
        print("RhymeWordProcessor hasn't been implemented yet.")

    def TBDrhymeWordsSortByNumberOfLetters(self, letterlist):
        '''Deliver rhyme word list sorted by the number of letters searched, so the rhyme word containing the highest number of letters corresponding the letter list given will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        letterlist:  -- (List of strings) List of letters to be counted

        returns:  -- (List of strings) List of rhyme words sorted by their number of letters given by letter list'''
        # TBD
        print("RhymeWordProcessor hasn't been implemented yet.")

    def TBDrhymeWordsSortByNumberOfLetterFrequency(self, letterlist):
        '''Deliver rhyme word list sorted by their frequency of letters searched, so the rhyme word containing the highest relative of letters corresponding the letter list given (letters searched out of all letters of word) will be the first word in the list returned
        !!Attention: Does not change the internal rhyme word list!!

        returns:  -- (List of strings) List of rhyme words sorted by frequency of letters given by letter list'''
        # TBD
        print("RhymeWordProcessor hasn't been implemented yet.")
