class RhymeWordExtractor:
    '''RhymeWordExtractor handles the extraction of rhyme words of lines of text given
    '''

    def __init__(self, textlines):
        '''Create a new instance of RhymeWordExtractor

        textlines:  -- (List of strings) List of textlines which we want to extract rhyme words for'''
        self.textlines = textlines

    def extractRhymeWords(self):
        '''Extract rhyme words of internal text lines

        returns:  -- (List of strings List of rhyme words extracted)'''
        # TBD
        rhymewordlist = []
        for verse in self.textlines:
            words = verse.split(' ')
            rhymeword = words[-1]
            rhymewordlist.append(rhymeword)
    
        print("RhymeWordExtractor hasn't been implemented yet.")
