import tkinter as tk
from tkinter import ttk

# Initilize window
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Numbra Development - GUI Sandbox")
# root.minsize(320,240)

# Color order
colororder = ["red", "blue", "green", "#ff9900", "cyan", "#93c46d", "#e06666", "#6d9ebb", "#ffd966", "#274e13",
              "#9900ff", "#e69138", "#0c343d", "#741b47"]

colorindex = 0

# Frames
set_frame = tk.Frame(root)
data_entry = tk.Frame(set_frame, background=colororder[colorindex], padx=0, pady=3, borderwidth=3, relief="raised")
extra_entry = tk.Frame(set_frame, background=colororder[colorindex], relief="raised")

data = []
# data entries
for n in range(20):
    data.append(tk.Entry(data_entry, width=7))
# error
error_entry = tk.Entry(extra_entry, width=3)
# unit
unit_entry = tk.Entry(extra_entry, width=3)
# LABELS
data_label_text = tk.Entry(data_entry, text="Value", justify=tk.CENTER, background="lightgrey", borderwidth=1,
                           relief="raised", width=7)
data_label_text.insert(tk.END, "Set 1")
error_label_text = tk.Label(extra_entry, text="Error", justify=tk.CENTER, background="lightgrey", relief="raised")
unit_label_text = tk.Label(extra_entry, text="Unit", justify=tk.CENTER, background="lightgrey", relief="raised")
# BUTTONS


def expand_func():
    if expand['text'] == '>':
        extra_entry.grid(column=1, row=0, sticky=tk.NSEW)
        expand.configure(text='<')
    else:
        extra_entry.grid_forget()
        expand.configure(text='>')



expand = tk.Button(set_frame, background="lightgrey", width=1, height=1, text=">", command=expand_func)
# ----
# GRID
# ----

# frame
set_frame.grid()
data_entry.grid(column=0, row=0, sticky=tk.NSEW)
extra_entry.grid(column=1, row=0, sticky=tk.NSEW)
# labels
data_label_text.grid(column=0, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)
error_label_text.grid(column=0, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)
unit_label_text.grid(column=1, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)

# entries
for i in range(len(data)):
    data[i].grid(row=i + 1, column=0, sticky=tk.W, padx=2)

error_entry.grid(row=1, column=0, sticky=tk.NSEW, padx=2)
unit_entry.grid(row=1, column=1, sticky=tk.NSEW, padx=2)

# buttons
expand.grid(row=0, column=2, rowspan=1, sticky=tk.NS)

# Hide Objects
extra_entry.grid_forget()

root.mainloop()
