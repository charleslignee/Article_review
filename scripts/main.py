# ---------------------
# Import packages
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import tkinter as tk
from tkinter import E, LEFT, RIGHT, W, filedialog as fd
from ArticleTools.ArticleTools import ArticleTools
import pandas as pd

to = ArticleTools()

root = tk.Tk()
root.geometry()
root.title("Article Review")



file_name = ''
def OpenFile():
    global file_name
    file_name = fd.askopenfilename(title = "Ouvrir",filetypes=(("bib files","*.bib"),("All files","*.*")))
    input_keys.insert(tk.END,",".join(to.BibtexFindCles(file_name)))
    input_keys_latex.insert(tk.END,",".join(['year','author','title','doi','keywords'] + to.BibtexFindCles(file_name)))
    label_file_name.config(text = "file: " + file_name)

def save_data():
    # Choix dossier de sauvegarde
    folder_name = fd.askdirectory(title="Enregistrer sous",initialdir=os.path.normpath(file_name[0:file_name.rfind(os.sep)]))
    # ---------------------
    # Récupération des données
    cles = input_keys.get().split(",")
    cles_latex = input_keys_latex.get().split(",")
    # ---------------------
    # Récupération du fichier .bib
    allData = pd.DataFrame()
    allData = to.ParserBibtexWithNote(file_name,cles)
    allData = allData.sort_values(by=['year'], ascending=False)
    # ---------------------
    # Ecriture du fichier '.csv' avec toutes les infos
    allData.to_csv(folder_name + os.sep + "all_data.csv",index=False)
    # ---------------------
    # Ecriture du tableau '.tex' et du fichier '.csv' avec les infos nécessaires
    allData[cles_latex].to_latex(folder_name + os.sep + "table.tex", index = False, escape = False)
    allData[cles_latex].to_csv(folder_name + os.sep + "table.csv", index = False)

img = tk.PhotoImage(file=to._adrArticleTools + os.sep + "docs" + os.sep + "bandeau_MCPIBAT.png")
label_img = tk.Label(root, image = img)
label_img.grid(row=0,column=0,columnspan=4)

empty_label = tk.Label(root,text=' ')
empty_label.grid(row=1,column=0,columnspan=3,pady=10)

label_keys = tk.Label(root, text = "Clés (exemple : country,climate,factor_of_study)")
label_keys.grid(row=2,column=0,columnspan=1)

input_keys = tk.Entry(root,width=100)
input_keys.grid(row=3,column=0,columnspan=1,padx=10)

empty_label = tk.Label(root,text=' ')
empty_label.grid(row=4,column=0,columnspan=3,pady=10)

label_keys_latex = tk.Label(root, text = "Clés retenues pour le tableau latex")
label_keys_latex.grid(row=5,column=0,columnspan=1)

input_keys_latex = tk.Entry(root,width=100)
input_keys_latex.grid(row=6,column=0,columnspan=1)

label_file_name = tk.Label(root)
label_file_name.grid(row=7,column=0,padx=20,sticky=W)

open_file = tk.Button(root, text = "Ouvrir le fichier", command=OpenFile)
open_file.grid(row=7,column=1,sticky=E,padx=5,pady=10)

button_save = tk.Button(root, text = "Enregistrer", command=save_data)
button_save.grid(row=7,column=2,sticky=W,pady=10)

button_close = tk.Button(root, text = "Fermer", command = root.destroy)
button_close.grid(row=7,column=3,padx=15,pady=10)

root.mainloop()