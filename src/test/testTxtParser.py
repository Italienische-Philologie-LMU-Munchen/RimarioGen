from txtparser import *

def test():
    testPath = "testData/CantoPrimoDC.txt"
    testTxtParser = TxtParser(testPath)
    testTxtParserResult = testTxtParser.parse()
    return testTxtParserResult
