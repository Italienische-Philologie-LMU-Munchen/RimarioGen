import tkinter as tk
from tkinter import ttk


class LegalNoticeGui(tk.Tk):
    '''LegalNoticeGui handles a small graphical window showing details about legal aspects of RimarioGen
    LegalNoticeGui iinherits from tkinter, so it is a tkinter application which should be possible to be run with standard Python installation without any pre-requisities'''

    def __init__(self):
        '''Create a new istane of LegalNoticeGui'''
        super().__init__()

        # Main legal text to be displayed
        self.legalText = '''RimarioGen
Version: 0.1.0.0 

Copyright: ©2024, GNU GPLv3 License 

Insitute of Italian Philology, LMU Munich. Collaborators: '''

        # List of libraries and copyright mentions to be displayed (read only mode!)
        self.legalTextLibraries = '''Software to analyze rhyme words in (Old) Italian texts 
        <br/><br/>
        The following resources have been used: 
        <br/><br/>        
        Pygal: https://github.com/Kozea/pygal,  LGPL 3.0-License
        <br/><br/>
        lxml: https://github.com/lxml/lxml, BSD License: Copyright (c) 2004 Infrae. All rights reserved.
        <br/><br/>
        Free Fontawesome icons: https://fontawesome.com/,  SIL OFL 1.1 license
        <br/><br/>'''
