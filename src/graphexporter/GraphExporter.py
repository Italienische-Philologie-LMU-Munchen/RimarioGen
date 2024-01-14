class GraphExporter:
    '''GraphExporter handles the export of result data produced by RimarioGen into a png graph file which is highly human-readable'''

    def __init__(self, lableData, data):
        '''Create a new instance of GraphExporter

        lableData:  -- (List of strings) Data to be used for the legend of png graph file
        data:       -- (List) Data to be used to create png graph file, must correspond to lableData'''
        self.lableData = lableData
        self.data = data

    def export(self, outputfile):
        '''Export data to png file given

        outputfile: -- (string) Path of file which graph is going to be written to. If file doesn't exist, it will be created. If it exists, it will be overwritten'''
        # TBD
        print("GraphExporter hasn't been implemented yet.")
