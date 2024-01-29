from rhymewordprocessor import *

def test():
    baseList = ['vita', 'oscura', 'smarrita', 'dura', 'stelle']
    testRhymeWordProcessor = RhymeWordProcessor(baseList)
    return testRhymeWordProcessor.sortAlphabeticallyLastLetter()
