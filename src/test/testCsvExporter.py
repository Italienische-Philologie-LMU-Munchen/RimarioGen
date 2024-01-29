from csvexporter import *
import os

def test():
    testCsvExporter = CsvExporter('rhymeword', ['vita', 'oscura', 'smarrita'])
    testCsvExporter.export(os.path.join(os.path.dirname(__file__), r"testData/testCsvExporter.csv"))
    return "TestCsvExporter tested!"
