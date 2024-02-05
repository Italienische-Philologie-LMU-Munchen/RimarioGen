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
        import re

        rhymewordlist = []
        for verse in self.textlines:
            words = verse.split(' ')
            rhymeword = words[-1]
            re.sub(r"^([^a-zA-Z])+", "", rhymeword)
            re.sub(r"$([^a-zA-Z])+", "", rhymeword)
            rhymewordlist.append(rhymeword)
        
        # re.sub(r"^\s*$", "", rhymewordlist)
        return(rhymewordlist)