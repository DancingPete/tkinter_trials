#!/usr/bin/env python
"""tkinter tabbed notebook geometry experiment.

Pierre Cassidy
2022-10-14
"""

import tkinter as tk
from tkinter import ttk


# Event functions
def main():
    root.mainloop()


def add_frame_1():
    notebook.insert(1, frame3, text="Three Again")


def kill_frame_1():
    notebook.forget(1)


# Geometry widgets
root = tk.Tk()
root.title = "Tabbed Notebook Experiment"

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
notebook.add(frame1, text="One")
notebook.add(frame2, text="Two")
notebook.insert(1, frame3, text="Three")

# Basic widgets
button1 = ttk.Button(
        frame1,
        text="Kill frame 1",
        command=kill_frame_1)
button1.pack()
button2 = ttk.Button(
        frame2,
        text="Add killed frame as 1",
        comman=add_frame_1)
button2.pack()


if __name__ == "__main__":
    main()
