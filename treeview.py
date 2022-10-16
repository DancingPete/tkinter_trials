#!/usr/bin/env python

"""tkinter treeview experimentation script.

Pierre Cassidy
2022-10-15
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview")

treeview = ttk.Treeview(root, height=4)
treeview.rowheight = 100
treeview.pack()
treeview.insert('', '0', 'Item1', text='Item 1')
treeview.insert('', '1', 'Item2', text='Item 2')
treeview.insert('', '2', 'Item3', text='Item 3')
treeview.insert('', 'end', 'Item4', text='Item 4')


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
