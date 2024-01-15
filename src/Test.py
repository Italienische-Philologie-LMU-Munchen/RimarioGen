import sys
from test import *

moduleNames = ('test.testTxtParser', 'test.testCsvExporter', 'test.testGraphExporter', 'test.testLemmatizer',
               'test.testRhymeWordExtractor', 'test.testRhymeWordProcessor', 'test.testTeiParser', 'test.testTxtExporter')

for module in moduleNames:
    print(sys.modules[module].test())

print("Test")

