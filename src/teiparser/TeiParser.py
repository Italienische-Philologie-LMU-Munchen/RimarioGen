class TeiParser:
    '''TeiParser handles the reading of text from a TEI XML file'''

    def __init__(self, inputfile):
        '''Create a new instance of TeiParser

        inputfile:  -- (string) Path to TEI XML file to be read and parsed'''
        self.inputfile = inputfile

    def parse(self):
        '''Parse textual content of internal TEI XML file

        returns:  -- (List of strings) All lines contained in TEI XML file (following P5 standard of TEI, usually identified by <l>-tags)'''
        # TBD
        print("TeiParser hasn't been implemented yet.")
