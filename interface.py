# interface.py

import tkinter as tk
from database import insert_facture

def launch_app():
    def submit():
        try:
            insert_facture(entry_date.get(), entry_desc.get(), var_type.get(), float(entry_montant.get()))
            result_label.config(text="Facture ajoutée !", fg="green")
        except Exception as e:
            result_label.config(text=f"Erreur : {e}", fg="red")

    window = tk.Tk()
    window.title("Saisie des factures")

    tk.Label(window, text="Date (YYYY-MM-DD)").pack()
    entry_date = tk.Entry(window)
    entry_date.pack()

    tk.Label(window, text="Description").pack()
    entry_desc = tk.Entry(window)
    entry_desc.pack()

    var_type = tk.StringVar()
    tk.Radiobutton(window, text="Revenu", variable=var_type, value="revenu").pack()
    tk.Radiobutton(window, text="Dépense", variable=var_type, value="depense").pack()

    tk.Label(window, text="Montant").pack()
    entry_montant = tk.Entry(window)
    entry_montant.pack()

    tk.Button(window, text="Valider", command=submit).pack()
    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()
