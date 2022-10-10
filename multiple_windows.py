#!/usr/bin/env python3

"""tkinter experimentation with multiple windows.

Pierre Cassidy
20201010
"""

# Standard library imports
import tkinter as tk
from tkinter import ttk

# Create root window
root = tk.Tk()
root.title("Main Root Window")
root.geometry("600x600+250+350")


# Create child window
child_window = tk.Tk()
child_window.title("Child Window")
child_window.geometry("600x600+350+450")

# Event handlers
def allow_resizable():
    child_window.resizable(width=True, height=True)

def deiconify():
    child_window.deiconify()

def destroy():
    child_window.destroy()

def forbid_resizable():
    child_window.resizable(width=False, height=False)

def iconify():
    child_window.iconify()

def lift():
    child_window.lift()

def lower():
    child_window.lower()


# Iconify button
button1 = ttk.Button(
        root,
        command=iconify,
        text="Iconify")
button1.grid(row=0, column=0)

button2 = ttk.Button(
        root,
        command=lift,
        text="Raise",)
button2.grid(row=1, column=0)

button3 = ttk.Button(
        root,
        command=lower,
        text="Lower",)
button3.grid(row=2, column=0)

button4 = ttk.Button(
        root,
        command=destroy,
        text="Destroy",)
button4.grid(row=3, column=0)

button5 = ttk.Button(
        root,
        command=deiconify,
        text="Deiconify",)
button5.grid(row=4, column=0)

button6 = ttk.Button(
        root,
        command=allow_resizable,
        text="Allow Resizable",)
button6.grid(row=5, column=0)

button7 = ttk.Button(
        root,
        command=forbid_resizable,
        text="Forbid Resizable",)
button7.grid(row=6, column=0)


def main():

    root.mainloop()

if __name__ == "__main__":
    main()
