#!/usr/bin/env python
"""tkinter experiment script for learning Panedwindow geometry widgets.

Pierre Cassidy
2022-10-14
"""

import tkinter as tk
from tkinter import ttk

def kill_frame_2():
    paned_window.forget(1)


# Define root window
root = tk.Tk()
root.title = "Paned Window Test"

# Define paned window
paned_window = ttk.Panedwindow(
        root,
        orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Define paned window frames
frame1 = ttk.Frame(
        paned_window,
        width=100,
        height=300,
        relief=tk.SUNKEN)
frame2 = ttk.Frame(
        paned_window,
        width=400,
        height=400,
        relief=tk.SUNKEN)
frame3 = ttk.Frame(
        paned_window,
        width=100,
        height=300,
        relief=tk.SUNKEN)

# Add frames to paned window
paned_window.add(frame1, weight=1)
paned_window.add(frame2, weight=4)
paned_window.insert(1, frame3)

# Add button to 'forget' pane
button = ttk.Button(
        frame1,
        text="Kill second frame",
        command=kill_frame_2)
button.pack()




def main():
    root.mainloop()


if __name__ == "__main__":
    main()
