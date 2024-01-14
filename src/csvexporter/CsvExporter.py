class CsvExporter:
    '''CsvExporter handles the export of result data produced by RimarioGen into a csv file which is human-readable but still ready for further programatical analysis'''

    def __init__(self, lableData, data):
        '''Create a new instance of CsvExporter

        lableData:  -- (List of strings) Data to be used for the headings of columns in csv file
        data:       -- (List) Data to be written to csv file, must correspond to lableData'''

        self.lableData = lableData
        self.data = data

    def export(self, outputfile):
        '''Export data to csv file given
        outputfile: -- (string) Path of file which data is going to be written to. If file doesn't exist, it will be created. If it exists, it will be overwritten'''

        # TBD
        print("CsvExporter hasn't been implemented yet.")
