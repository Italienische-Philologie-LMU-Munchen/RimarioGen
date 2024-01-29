from teiparser import *
import os

def test():
    testTeiParser = TeiParser(os.path.join(os.path.dirname(__file__), r"testData/Commedia.xml"))
    return testTeiParser.parse()
