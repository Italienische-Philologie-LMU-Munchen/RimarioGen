from txtexporter import *
import os

def test():
    testTxtExporter = TxtExporter('rhymeword', ['vita', 'oscura', 'smarrita'])
    testTxtExporter.export(os.path.join(os.path.dirname(__file__), r"testData/testTxtExporter.txt"))
    return "TestTxtExporter tested!"
