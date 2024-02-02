import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter.filedialog import askopenfilename
from tkinter import Checkbutton
from tkinter import Listbox


class RimarioGenGui(tk.Tk):
    '''RimarioGenGui handles a graphical interface to be displayed to the user, so (s)he can use the functionality of RimarioGen easily
    RimarioGenGui iinherits from tkinter, so it is a tkinter application which should be possible to be run with standard Python installation without any pre-requisities'''

    def __init__(self):
        '''Create a new instance of RimarioGenGui'''
        self.filename = ''

        tk.Tk.__init__(self)
        self.baseWidth = 800
        self.baseHeight = 600
        self.setupWindow()

    def setupWindow(self):
        '''Setup the configuration of windwo/graphical interface, e.g. buttons, their positioning, their layout etc.'''
        # Fixed geometry for startup of application
        self.geometry(str(self.baseWidth)+'x'+str(self.baseHeight)+'+5+40')
        self.resizable(False, False)

        self.title('Rimario Generator')

        self.grid_propagate(0)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.setupFileFrame()
        self.setupAvailableMethodsFrame()
        self.setupMethodChangeFrame()
        self.setupChosenMethodsFrame()
        self.setupExportFrame()
        self.setupRunFrame()

    def setupFileFrame(self):
        fileWidth = self.baseWidth//5*2 - 10
        fileHeight = self.baseHeight//5*2
        self.fileFrame = Frame(
            self, bg="blue", width=fileWidth, height=fileHeight)
        self.fileFrame.grid_propagate(0)
        self.fileFrame.grid(row=0, rowspan=2, column=0, columnspan=2,
                            padx=5, pady=5)
        self.fileFrame.grid_columnconfigure(2, weight=1)
        self.fileFrame.grid_rowconfigure(5, weight=1)

        self.lbFileSelect = Label(
            self.fileFrame, text="Select a file")
        self.lbFileSelect.grid(row=0, column=0, padx=5, pady=5, sticky='NW')

        self.btFileSelect = Button(
            self.fileFrame, text="Choose a file", command=self.btFileSelectClick)
        self.btFileSelect.grid(row=1, padx=5, pady=5, sticky='W')

        self.lbFileChosen = Label(
            self.fileFrame, text="File chosen:")
        self.lbFileChosen.grid(row=3, column=0, padx=5, pady=5, sticky='W')

        self.lbFileChosen = Label(
            self.fileFrame, text="")
        self.lbFileChosen.grid(row=4, column=0, padx=5, pady=5, sticky='W')

    def setupAvailableMethodsFrame(self):
        availableMethodsWidth = self.baseWidth//5 - 10
        availableMethodsHeight = self.baseHeight//5*4
        self.availableMethodsFrame = Frame(
            self, bg="red", width=availableMethodsWidth, height=availableMethodsHeight)
        self.availableMethodsFrame.grid_propagate(0)
        self.availableMethodsFrame.grid(
            row=0, rowspan=4, column=2, padx=5, pady=5)
        self.availableMethodsFrame.grid_columnconfigure(1, weight=1)
        self.availableMethodsFrame.grid_rowconfigure(5, weight=1)

        self.lboxAvailableMethods = Listbox(
            self.availableMethodsFrame, height=10)
        self.lboxAvailableMethods.grid(
            row=0, column=0, padx=5, pady=5, sticky='N')

    def setupMethodChangeFrame(self):
        methodChangeWidth = self.baseWidth//5 - 10
        methodChangeHeight = self.baseHeight//5*4
        self.methodChangeFrame = Frame(
            self, bg="green", width=methodChangeWidth, height=methodChangeHeight)
        self.methodChangeFrame.grid_propagate(0)
        self.methodChangeFrame.grid(row=0, rowspan=4, column=3, padx=5, pady=5)
        self.methodChangeFrame.grid_columnconfigure(0, weight=1)
        self.methodChangeFrame.grid_rowconfigure(5, weight=1)

        self.lbMethodChange = Label(
            self.methodChangeFrame, text="Select analysis methods")
        self.lbMethodChange.grid(row=0, column=0, padx=5, pady=5, sticky='NW')

        self.btAddMethod = Button(
            self.methodChangeFrame, text="-->", command=self.btAddMethodClick)
        self.btAddMethod.grid(row=1, padx=5, pady=5, sticky='WE')

        self.btRemoveMethod = Button(
            self.methodChangeFrame, text="<--", command=self.btRemoveMethodClick)
        self.btRemoveMethod.grid(row=2, padx=5, pady=5, sticky='WE')

    def setupChosenMethodsFrame(self):
        chosenMethodsWidth = self.baseWidth//5 - 10
        chosenMethodsHeight = self.baseHeight//5*4
        self.chosenMethodsFrame = Frame(
            self, bg="yelloW", width=chosenMethodsWidth, height=chosenMethodsHeight)
        self.chosenMethodsFrame.grid_propagate(0)
        self.chosenMethodsFrame.grid(
            row=0, rowspan=4, column=4, padx=5, pady=5)
        self.chosenMethodsFrame.grid_columnconfigure(1, weight=1)
        self.chosenMethodsFrame.grid_rowconfigure(5, weight=1)

        self.lboxChosenMethods = Listbox(
            self.chosenMethodsFrame, height=10)
        self.lboxChosenMethods.grid(
            row=0, column=0, padx=5, pady=5, sticky='N')

    def setupExportFrame(self):
        exportWidth = self.baseWidth//5*2 - 10
        exportHeight = self.baseHeight//5*2
        self.exportFrame = Frame(
            self, bg="orange", width=exportWidth, height=exportHeight)
        self.exportFrame.grid_propagate(0)
        self.exportFrame.grid(row=2, rowspan=2, column=0,
                              columnspan=2, padx=5, pady=5)
        self.exportFrame.grid_columnconfigure(1, weight=1)
        self.exportFrame.grid_rowconfigure(5, weight=1)

        self.lbExportSelect = Label(
            self.exportFrame, text="Select an export format")
        self.lbExportSelect.grid(row=0, column=0, padx=5, pady=5, sticky='NW')

        self.cbExportTxt = Checkbutton(
            self.exportFrame, text="Txt")
        self.cbExportTxt.grid(row=1, padx=5, pady=5, sticky='W')

        self.cbExportCsv = Checkbutton(
            self.exportFrame, text="Csv")
        self.cbExportCsv.grid(row=2, padx=5, pady=5, sticky='W')

    def setupRunFrame(self):
        runWidth = self.baseWidth - 10
        runHeight = self.baseHeight//5
        self.runFrame = Frame(
            self, bg="turquoise", width=runWidth, height=runHeight)
        self.runFrame.grid_propagate(0)
        self.runFrame.grid(row=5, columnspan=5, column=0, padx=5, pady=5)
        self.runFrame.grid_columnconfigure(0, weight=1)
        self.runFrame.grid_rowconfigure(0, weight=1)

        self.btRun = Button(
            self.runFrame, text="Generate Rimario", command=self.btRunClick)
        self.btRun.grid(columnspan=5,
                        padx=5, pady=5, sticky='WE')

    def btFileSelectClick(self):
        maxlength = 40
        filepath = askopenfilename()
        if len(filepath) > maxlength:
            self.filename = '...' + filepath[maxlength*-1:]
        else:
            self.filename = filepath
        self.lbFileChosen.config(text=self.filename)

    def btRunClick(self):
        print("")

    def btAddMethodClick(self):
        print("")

    def btRemoveMethodClick(self):
        print("")


def main():
    # Start application and load main window
    window = RimarioGenGui()
    # Show window and execute application
    window.mainloop()


if __name__ == "__main__":
    main()
