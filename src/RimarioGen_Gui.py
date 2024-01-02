import tkinter as tk
from tkinter import ttk


class RimarioGenGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.setupWindow()

    def setupWindow(self):
        # TBD
        print("RimarioGenGui hasn't been implemented yet.")


def main():
    # Start application and load main window
    window = RimarioGenGui()
    # Show window and execute application
    window.mainloop()


if __name__ == "__main__":
    main()
