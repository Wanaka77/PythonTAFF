import os
import tkinter as tk
from tkinter import ttk

def search_files():
    directory_path = dir_entry.get()
    extension = type_file_dropdown.get()

    result_listbox.delete(0, tk.END)

    for file_name in os.listdir(directory_path):
        if file_name.endswith(extension):
            result_listbox.insert(tk.END, file_name)

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Recherche de fichiers SVG")
root.geometry("600x400")
root.configure(bg="black")

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='LienSVG')

type_file_label = ttk.Label(tab1, text="Type de fichier :", font=("TkDefaultFont", 10))
type_file_label.grid(column=0, row=0, padx=10, pady=10, sticky="W")

type_file_dropdown = ttk.Combobox(tab1, values=[".ai", ".svg"], width=5)
type_file_dropdown.current(1)
type_file_dropdown.grid(column=1, row=0, padx=10, pady=10, sticky="W")

dir_label = ttk.Label(tab1, text="Répertoire :", font=("TkDefaultFont", 10))
dir_label.grid(column=0, row=1, padx=10, pady=10, sticky="W")

dir_entry = ttk.Entry(tab1, width=40)
dir_entry.grid(column=1, row=1, padx=10, pady=10, sticky="W")

execute_button = ttk.Button(tab1, text="Rechercher", command=search_files)
execute_button.grid(column=1, row=2, padx=10, pady=10, sticky="W")

tab_control.pack(expand=1, fill="both")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Onglet2')

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Onglet3')

result_frame = ttk.Frame(root)
result_frame.pack(padx=10, pady=10, expand=1, fill="both")

result_label = ttk.Label(result_frame, text="Résultats de la recherche :", font=("TkDefaultFont", 10))
result_label.pack(pady=10)

result_listbox = tk.Listbox(result_frame)
result_listbox.pack(padx=10, pady=10, expand=1, fill="both")

quit_button = ttk.Button(result_frame, text="Quitter", command=quit_program)
quit_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
