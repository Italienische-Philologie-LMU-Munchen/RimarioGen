import sys
from test import *

#moduleNames = ('test.testTxtParser', 'test.testCsvExporter', 'test.testGraphExporter', 'test.testLemmatizer',
               #'test.testRhymeWordExtractor', 'test.testRhymeWordProcessor', 'test.testTeiParser', 'test.testTxtExporter')
moduleNames = ('test.testRhymeWordExtractor', 'test.testCsvExporter')
for module in moduleNames:
    print(module + ":\n")
    print(sys.modules[module].test())
