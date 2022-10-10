#!/usr/bin/env python

"""Test application for experimenting with themed tkinter widgets.

Pierre Cassidy
20221007
"""

# Standard library imports
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = ttk.Label(root, text="Big Fart")
button = ttk.Button(root, text="Click Me!")
label.pack()
button.pack()
root.mainloop()
