#!/usr/bin/env python

"""Tkinter test GUI for using frames.

Pierre Cassidy
2022-10-09
"""

import tkinter as tk
from tkinter import ttk

# Define root window
root = tk.Tk()


# Define test frame
frame = ttk.Frame(
        root,
        height=100,
        width=100,
        padding=(30, 15),
        relief=tk.RAISED,)
frame.config()
frame.pack()

# Define a button as child to frame
button = ttk.Button(
        frame,
        text="Press Me")
button.grid()

# Define a 'label frame' to group widgets
label_frame = ttk.LabelFrame(
        root,
        height=100,
        width=200,
        text="My Label")
label_frame.pack()


# Define the main function
def main():
    root.mainloop()


if __name__ == "__main__":
    main()
