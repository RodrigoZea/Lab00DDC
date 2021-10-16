import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import os
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PyDecaf import check


default_dir = 'D:\\UVG\\5toAno\\comp2\\Lab00DDC\\Decaf\\test_files'

def update_filepath(file):
    filepath_temp = file

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

    update_filepath(filepath)
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

    update_filepath(filepath)
    window.title(f"Decaf Editor - {filepath}")

def run_antlr():
    """Run a decaf file and perform a lexical analysis """
    # Check if it already has a filepath
    # If it doesnt have a filepath, save with temp.decaf name
    # Overwrite either way
    if (filepath_temp  == None):
        filepath = default_dir + "\\temp.decaf"

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

    label_errors.config(text="")
    window.title(f"Decaf Editor - Checking {filepath}")

    errors, quads = check(filepath)
    n = len(errors)

    element = ''
    for key, value in errors.items():
        element = element + key[1] + " at line (" + str(key[0]) + "): " + value +'\n'

    if (n == 0): element = "No errors!"
    label_errors.config(text=element)  

    element = ''
    for quad in quads:
        element = element + quad

    txt_codegen.delete(1.0, tk.END)
    txt_codegen.insert(tk.END, element)


filepath_temp = None
window = tk.Tk()
window.title("Decaf Editor")
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Syntax Analysis')
tabControl.add(tab2, text ='Intermediate Code Generation')
tabControl.pack(expand = 1, fill ="both")

tab1.rowconfigure(0, minsize=800, weight=1)
tab1.columnconfigure(1, minsize=800, weight=1)
tab1.columnconfigure(2, minsize=700, weight=1)

tab2.rowconfigure(0, minsize=800, weight=1)
tab2.columnconfigure(0, minsize=800, weight=1)

fr_buttons = ttk.Frame(tab1)
fr_buttons.grid(row=0, column=0, stick="ns")
btn_open = ttk.Button(fr_buttons, text="Open", command=open_file)
btn_open.pack()
btn_save = ttk.Button(fr_buttons, text="Save As...", command=save_file)
btn_save.pack()
btn_run = ttk.Button(fr_buttons, text="Run...", command=run_antlr)
btn_run.pack()

txt_edit = scrolledtext.ScrolledText(tab1)
txt_edit.grid(row=0, column=1, sticky="nsew")

label_errors = ttk.Label(tab1, text="Errors")
label_errors.grid(row=0, column=2, sticky="nw", padx=5, pady=5)

# Codegen
txt_codegen = scrolledtext.ScrolledText(tab2)
txt_codegen.grid(row=0, column=0, sticky="nsew")

window.mainloop()
