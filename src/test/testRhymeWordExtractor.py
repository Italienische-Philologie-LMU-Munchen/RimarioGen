from rhymewordextractor import *

def test():    
    testLines = ['Nel mezzo del cammin di nostra vita', 'mi ritovai in una selva oscura', 'Voi ch\'ascoltate le mie rime sparse']
    testExtractor = RhymeWordExtractor(testLines)
    testExtractorResult = testExtractor.extractRhymeWords()
    return testExtractorResult
