#!/usr/bin/env python
"""Simple GUI app to practice using Tkinter.

Pierre Cassidy
20221008
"""

# Standard library import
import tkinter as tk
from tkinter import ttk

# Main app as class
class HelloApp:
    
    def __init__(self, master):

        self.label = ttk.Label(master, text="Hello, Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)

        button_texas = ttk.Button(
                master,
                text="Texas",
                command=self.texas_hello)
        button_texas.grid(row=1, column=0)

        button_hawaii = ttk.Button(
                master,
                text="Hawaii",
                command=self.hawaii_hello)
        button_hawaii.grid(row=1, column=1)

    def texas_hello(self):
        self.label.config(text="Howdy, Tkinter!")

    def hawaii_hello(self):
        self.label.config(text="Aloha, Tkinter!")


# Main function for running app
def main():
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()

# Run app when module called directly
if __name__ == '__main__':
    main()
