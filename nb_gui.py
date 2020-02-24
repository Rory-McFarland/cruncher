"""
nb_gui
Numbera Graphical User Interface
    Default GUI for Cruncher to interface with the user graphically and through HID's

    By Rory McFarland, Dr. Darci Snowden
    Developed at Central Washington University

    15 Oct 2019
    Rev 1.0.0, compiled 9 July 2019
"""


#data grid
sheet_frame = ttk.Frame(root)
sheet_frame.grid(sticky = tk.N+tk.S+tk.E+tk.W)
#cell canvas
sheet_canvas = tk.Canvas(sheet_frame)
sheet_canvas.grid(pady=(5, 0), sticky = tk.N+tk.W)
sheet_canvas.grid_rowconfigure(0, weight=1)
sheet_canvas.grid_columnconfigure(0, weight=1)
#scrollable region
scrollable_frame = ttk.Frame()
scrollable_frame.grid(sticky = tk.N+tk.S+tk.E+tk.W)
y_scrollbar = ttk.Scrollbar(sheet_canvas, orient = tk.VERTICAL, command = sheet_canvas.yview)
x_scrollbar = ttk.Scrollbar(sheet_canvas, orient = tk.HORIZONTAL, command = sheet_canvas.xview)


scrollable_frame.bind(
    "<Configure>",
    lambda e: sheet_canvas.configure(
        scrollregion=sheet_canvas.bbox(tk.ALL)
    )
)

sheet_canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

sheet_canvas.configure(yscrollcommand=y_scrollbar.set, xscrollcommand = x_scrollbar.set)

#grid configureation
rows = 26
columns = 100
for i in range(rows):
    for j in range(columns):
        ttk.Entry(scrollable_frame).grid(row=i, column=j+1)
# pack everything
sheet_frame.grid()
sheet_canvas.grid()
y_scrollbar.grid(sticky=tk.E)
x_scrollbar.grid(sticky=tk.E+tk.S)



"""
Copyright 2019 Rory McFarland

This file is part of Cruncher.

Cruncher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Cruncher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Cruncher. If not, see <https://www.gnu.org/licenses/>.
"""