import tkinter as tk
from tkinter import PhotoImage
import os
from pathlib import Path
from tkinter import Label
from tkinter.scrolledtext import ScrolledText


class LegalNoticeGui(tk.Tk):
    '''LegalNoticeGui handles a small graphical window showing details about legal aspects of RimarioGen
    LegalNoticeGui iinherits from tkinter, so it is a tkinter application which should be possible to be run with standard Python installation without any pre-requisities'''

    def __init__(self):
        '''Create a new istane of LegalNoticeGui'''
        tk.Tk.__init__(self)

        self.baseWidth = 450
        self.baseHeight = 450

        # Title of application window and icon
        self.title("Rimario Generator - Legal Notice")

        # Icon handling
        file = str(Path(os.path.dirname(__file__)).parent.absolute() /
                   'assets' / 'clipboard-list-solid.png')
        # self.iconphoto(False, PhotoImage(file=file))

        # Fixed geometry for startup of application
        self.geometry(str(self.baseWidth)+'x'+str(self.baseHeight)+'+5+40')
        self.resizable(False, False)

        self.grid_propagate(0)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(5, weight=1)

        # Heading for legal text to be displayed
        self.lbLegalTextHeading = Label(self, text='Legal Notice:')
        self.lbLegalTextHeading.grid(
            row=0, column=0, padx=5, pady=5, sticky='NW')

        # Main legal text to be displayed
        self.legalText = '''Rimario Generator

Version: 0.1.0.0

Copyright: ©2024, GNU GPLv3 License

Insitute of Italian Philology, LMU Munich.
Collaborators: Veronika Diem, Sheila Incarbone, Sascha Resch'''
        self.lbLegalText = Label(self, text=self.legalText, justify='left')
        self.lbLegalText.grid(row=1, column=0, padx=5, pady=5, sticky='NW')

        # List of libraries and copyright mentions to be displayed (read only mode!)
        self.legalTextLibraries = '''Software to analyze rhyme words in (Old) Italian texts 
\n
The following resources have been used: 
\n     
lxml: https://github.com/lxml/lxml, BSD License\n
Copyright (c) 2004 Infrae. All rights reserved.
\n
Pigar: https://github.com/damnever/pigar, BSD License\n
Copyright (c) 2020 XiaoChao Dong (@damnever) <dxc.wolf@gmail.com>\n
All rights reserved.
\n
Free Fontawesome icons: https://fontawesome.com/\n
SIL OFL 1.1 license
\n
Draw.io Desktop: https://github.com/jgraph/drawio-desktop
Apache 2.0 licence'''

        self.txtlegalTextLibraries = ScrolledText(
            self, width=self.baseWidth//9, height=self.baseHeight//30, font=("Helvetica", 10), )
        self.txtlegalTextLibraries.insert(tk.END, self.legalTextLibraries)
        self.txtlegalTextLibraries.configure(state=tk.DISABLED)
        self.txtlegalTextLibraries.grid(
            row=2, column=0, padx=5, pady=5, sticky='NW')
