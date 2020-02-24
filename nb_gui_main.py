import tkinter as tk
from tkinter import ttk

#Initilize window
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Numbera")
root.minsize(320,240)

# Theming
colororder = ["red", "blue", "green", "#ff9900", "cyan", "#93c46d", "#e06666", "#6d9ebb", "#ffd966", "#274e13",
              "#9900ff", "#e69138", "#0c343d", "#741b47"]

colorindex = 0

# =======
# CLASSES
# =======

class data_entry:
    def __init__(self):
        # Frames
        self.set_frame = tk.Frame(root)
        self.data_entry = tk.Frame(self.set_frame, background=colororder[colorindex], padx=0, pady=3, borderwidth=3, relief="raised")
        self.extra_entry = tk.Frame(self.set_frame, background=colororder[colorindex], relief="raised")

        self.data = []
        # data entries
        for n in range(20):
            self.data.append(tk.Entry(self.data_entry, width=7))
        # error
        self.error_entry = tk.Entry(self.extra_entry, width=3)
        # unit
        self.unit_entry = tk.Entry(self.extra_entry, width=3)
        # LABELS
        self.data_label_text = tk.Entry(self.data_entry, text="Value", justify=tk.CENTER, background="lightgrey", borderwidth=1,
                                   relief="raised", width=7)
        self.data_label_text.insert(tk.END, "Set 1")
        self.error_label_text = tk.Label(self.extra_entry, text="Error", justify=tk.CENTER, background="lightgrey", relief="raised")
        self.unit_label_text = tk.Label(self.extra_entry, text="Unit", justify=tk.CENTER, background="lightgrey", relief="raised")

        def expand_func():
            if self.expand['text'] == '>':
                self.extra_entry.grid(column=1, row=0, sticky=tk.NSEW)
                self.expand.configure(text='<')
            else:
                self.extra_entry.grid_forget()
                self.expand.configure(text='>')

        self.expand = tk.Button(self.set_frame, background="lightgrey", width=1, height=1, text=">", command=expand_func)
        # ----
        # GRID
        # ----
    def draw(self, master, columnindex, rowindex):
        # frame
        self.set_frame.grid()
        self.data_entry.grid(column=0, row=0, sticky=tk.NSEW)
        self.extra_entry.grid(column=1, row=0, sticky=tk.NSEW)
        # labels
        self.data_label_text.grid(column=0, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)
        self.error_label_text.grid(column=0, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)
        self.unit_label_text.grid(column=1, row=0, columnspan=1, sticky=tk.NSEW, padx=2, pady=3)

        # entries
        for i in range(len(self.data)):
            self.data[i].grid(row=i + 1, column=0, sticky=tk.W, padx=2)

        self.error_entry.grid(row=1, column=0, sticky=tk.NSEW, padx=2)
        self.unit_entry.grid(row=1, column=1, sticky=tk.NSEW, padx=2)

        # buttons
        self.expand.grid(row=0, column=2, rowspan=1, sticky=tk.NS)

        # Hide Objects
        self.extra_entry.grid_forget()
        # Draw
        self.set_frame.grid(column = colorindex, row=rowindex, sticky=tk.N+tk.W)

#menu bar
menubar = tk.Menu(root)
#file menu
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
#edit menu
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
#view menu
viewmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='View', menu=viewmenu)
#help menu
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
#add menubar
root.config(menu=menubar)

#cell frame
cell_frame = tk.Frame(root)
cell_frame.grid(sticky = tk.N+tk.S+tk.E+tk.W)

#cell canvas
#sheet_canvas = tk.Canvas(cell_frame)
#sheet_canvas.grid(sticky = tk.N+tk.W)
#sheet_canvas.grid_rowconfigure(0, weight=1)
#sheet_canvas.grid_columnconfigure(0, weight=1)


#scrollbar setup
#cell_frame.bind(
#    "<Configure>",
#    lambda e: sheet_canvas.configure(
#        scrollregion=sheet_canvas.bbox(tk.ALL)
#    )
#)

#sheet_canvas.configure(yscrollcommand=y_scrollbar.set, xscrollcommand = x_scrollbar.set)

#grids
grid_rows = 40
grid_columns = 20
cell_frame.grid_rowconfigure(grid_rows, weight=1)
cell_frame.columnconfigure(grid_columns, weight=1)

for i in range(grid_rows):
    for j in range(grid_columns):
        tk.Frame(cell_frame, highlightbackground="black",highlightthickness=1,width = 90, height = 24).grid(row=i, column=j+1, sticky=tk.N+tk.W)

#sheet_canvas.grid(sticky=tk.NW)
cell_frame.grid()
data_entry().draw(root,0,0)
data_entry().draw(root,1,0)
data_entry().draw(root,2,0)
#Window loop
root.mainloop()

# ---------
# FUNCTIONS
# ---------

#def getgrid():






