# -*- coding: utf-8 -*-
# @brief Récupére les inforamtions depuis le fichier '.ris'
"""
Created on Wed 7 9:15:04 2021
@author: Lionel
"""
#%%
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import pandas as pd
from RISparser import readris

# ---------------------
# Chargement de la classe et du fichier de bibliographie
from ArticleTools.ArticleTools import ArticleTools
to = ArticleTools()
filenameBib = "simu1.bib"
adr = to._adrArticleTools + os.sep + "Data" + os.sep
adrStore = to._adrArticleTools + os.sep + "_store" + os.sep
#%%
# ---------------------
# Récupération du fichier .ris
allData = pd.DataFrame()
lesCles = ["Infos","Analyse","Dechet","Note"]
allData = to.ParserBibtexWithNote(adr+filenameBib,lesCles)
allData = allData.sort_values(by=['year'], ascending=False)
allData.to_csv(adrStore + 'simu1.csv',index=False)   
