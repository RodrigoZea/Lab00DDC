import tkinter as tk
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyDecaf import check

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Decaf", "*.decaf")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Decaf Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="decaf",
        filetypes=[("Decaf", "*.decaf")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Decaf Editor - {filepath}")

def run_antlr():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Decaf", "*.decaf")]
    )
    if not filepath:
        return

    label_errors.config(text="")
    window.title(f"Decaf Editor - Checking {filepath}")


    errors = check(filepath)
    n = len(errors)

    element = ''
    for i in range(n):
        element = element + errors[i]+'\n'

    label_errors.config(text=element)

window = tk.Tk()
window.title("Decaf Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.columnconfigure(2, minsize=400, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_run = tk.Button(fr_buttons, text="Run...", command=run_antlr)

label_errors = tk.Label(window, text="oijaosdfjasdf")

btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_run.grid(row=2, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
label_errors.grid(row=0, column=2, sticky="nw", padx=5, pady=5)


window.mainloop()
