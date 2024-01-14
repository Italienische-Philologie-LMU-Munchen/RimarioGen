import tkinter as tk
from tkinter import ttk


class RimarioGenGui(tk.Tk):
    '''RimarioGenGui handles a graphical interface to be displayed to the user, so (s)he can use the functionality of RimarioGen easily
    RimarioGenGui iinherits from tkinter, so it is a tkinter application which should be possible to be run with standard Python installation without any pre-requisities'''

    def __init__(self):
        '''Create a new instance of RimarioGenGui'''
        tk.Tk.__init__(self)
        self.setupWindow()

    def setupWindow(self):
        '''Setup the configuration of windwo/graphical interface, e.g. buttons, their positioning, their layout etc.'''
        # TBD
        print("RimarioGenGui hasn't been implemented yet.")


def main():
    # Start application and load main window
    window = RimarioGenGui()
    # Show window and execute application
    window.mainloop()


if __name__ == "__main__":
    main()
