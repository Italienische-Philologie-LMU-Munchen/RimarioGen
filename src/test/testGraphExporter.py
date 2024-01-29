from graphexporter import *
import os

def test():
    testGraphExporter = GraphExporter('rhymeword', ['vita', 'oscura', 'smarrita'])
    testGraphExporter.export(os.path.join(os.path.dirname(__file__), r"testData/testGraphExporter.png"))
    return "TestGraphExporter tested!"
