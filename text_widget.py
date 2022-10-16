#!/usr/bin/env python

"""tkinter experimentation with the Text widget.

Pierre Cassidy
2022-10-15
"""

import tkinter as tk
from tkinter import ttk


def delete1():
    text.delete("1.0", "1.0 lineend")


def delete2():
    text.delete("2.0", "2.0 lineend + 1 chars")


def text_replace1():
    text.replace("1.0", "1.0 lineend", "This line has been replaced.")


# Root definition
root = tk.Tk()
root.title("Text Widget Experiment")

# Frame definition
frame = ttk.Frame(
        root,
        height="1000",
        width="1000")
frame.pack()

# Text widget definition
text = tk.Text(
        frame,
        height=10,
        width=50,
        wrap="word",)  # Wraps at word instead of character
text.pack()
text.insert('1.0', "First line.\n")
text.insert('2.0', "Second line.\n")
text.insert('3.0', "Third line.\n")


# Button definition
button_delete1 = ttk.Button(
        frame,
        text="Delete line 1",
        command=delete1)
button_delete2 = ttk.Button(
        frame,
        text="Delete line 2",
        command=delete2)
button_replace1 = ttk.Button(
        frame,
        text="Replace line 1",
        command=text_replace1)
button_delete1.pack()
button_delete2.pack()
button_replace1.pack()


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
