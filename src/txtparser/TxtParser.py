class TxtParser:
    '''TxtParser handles the reading of text from a raw txt file'''

    def __init__(self, inputfile):
        '''Create a new instance of TxtParser
        inputfile:  -- (string) Path to txt file to be read and parsed'''
        self.inputfile = inputfile

    def parse(self):
        '''Parse textual content of internal txt file
        returns:  -- (List of strings) All lines contained in txt file (single lines separated by linebreak in txt file)'''

        try:
            with open(self.inputfile, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return lines
        except FileNotFoundError:
            print(f"File not found: {self.inputfile}")
            return []  # leere Liste im Falle eines Fehlers
