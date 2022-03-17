# -*- coding: utf-8 -*-
# @brief Récupére les inforamtions depuis le fichier '.ris'
"""
Created on Wed 7 9:15:04 2021
@author: Lionel
"""
#%%
# ---------------------
# Import packages
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import pandas as pd
from RISparser import readris

#%%
# ---------------------
# Chargement de la classe et du fichier de bibliographie
from ArticleTools.ArticleTools import ArticleTools
to = ArticleTools()
filenameBib = "simu.bib"
adr = to._adrArticleTools + os.sep + "Data" + os.sep
adrStore = to._adrArticleTools + os.sep + "_store" + os.sep
#%%
# ---------------------
# Récupération du fichier .ris
allData = pd.DataFrame()
lesCles = ["material","melting","solidification","type_MCP","lh","cond_therm","density","country","weather","software","method","scale","model","Num_vs_Expe","nb_citing","comment","lu_par"]
allData = to.ParserBibtexWithNote(adr+filenameBib,lesCles)
allData = allData.sort_values(by=['year'], ascending=False)
# Ecriture du fichier '.csv' avec toutes les infos
allData.to_csv(adrStore + 'Biblio_simu.csv',index=False)   

# %%
# ---------------------
# Ecriture du tableau '.tex' et du fichier '.csv' avec les infos nécessaires
allData[["id","year","country","software","method","model"]].to_latex(adrStore + "table.tex", index = False, escape = False)
allData[["id","year","country","software","method","model"]].to_csv(adrStore + "table.csv", index = False)
# %%

# %%
