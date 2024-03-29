class TxtExporter:
    '''TxtExporter handles the export of result data produced by RimarioGen into a txt file which is highly human-readable but rather difficult to be processed by a machine'''

    def __init__(self, lableData, data):
        '''Create a new instance of TxtExporter

        lableData:  -- (List of strings) Data to be used for the legend of txt file
        data:       -- (List) Data to be used to create txt file, must correspond to lableData'''
        self.lableData = lableData
        self.data = data

    def export(self, outputfile):
        '''Export data to txt file given

        outputfile: -- (string) Path of file which data is going to be written to. If file doesn't exist, it will be created. If it exists, it will be overwritten'''

        # Lisa

        f = open(outputfile, "w", encoding="utf-8")

        f.write(self.lableData)
        f.write("\n\n")

        for rhymeword in self.data:
            f.write(rhymeword)
            f.write("\n")

        f.close()
