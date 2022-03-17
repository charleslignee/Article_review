# -*- coding: utf-8 -*-
# Created on Wed Jan 5 14:38:00:2022
# @package ArticleTools.ArticleTools
# @brief Outils pour le traitement des informations des articles
# au format bibtex et csv
# @author: lionel
# /updated by charles on Thu Feb 24
# ---------------------
import bibtexparser
import pandas as pd
import os

class ArticleTools():

    def __init__(self):
        self._adrArticleTools = self.__AdresseDuModule()

    # Définit l'adresse où se trouve le module
    def __AdresseDuModule(self):
        """ Recupére l'adresse "de ce fichier" et on descend 
        de deux crans

        Sortie
        ------
            string : adresse du module
        """        
        adrFile = os.path.dirname(os.path.realpath(__file__))
        adr = adrFile[0:adrFile.rfind(os.sep)]
        return adr
    
    ## Récupére les informations du fichier bibtex  
    def ParserBibtexWithNote(self,filename,lesCles):
        """ Regroupe les informations du fichier .bib dans une dataframe. Le fichier '.bib'
        peut comporter des notes à conserver suivant une codification. La codification
        est établit avec la clé 'annote' et suit la structuration suivante :
            - le délimiteur des entités est "\n"
            - le délimiteur des mots clés ":"
            - le délimiteur des valeurs est ","

        Arguments
        ---------
            filename [str] : nom du fichier à charger
            lesCles [list] : nom des mots clés à considérer

        Sortie
        ------
            [dataframe] : informations provenant du fichier bibtex
        """        
        with open(filename) as bibtex_file:
            bibtex_str = bibtex_file.read()
            
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.loads(bibtex_str,parser=parser)
        allData = pd.DataFrame()
        for entry in bib_database.entries:
            # ================
            # Elements d'identification du fichier
            ticket = {}
            if 'ID' in entry.keys():
                ticket.update({"id": "\cite{" + entry['ID'] + "}"})
            for cle in ['year','author','title','doi','keywords']:
                if cle in entry.keys():
                    ticket.update({cle:entry[cle]})
            
            # ================
            # Traitements des notes de l'article
            if 'annote' in entry.keys():
                notes = {}
                for uneNote in entry['annote'].split('\n') :
                    for cle in lesCles:
                        if ":" in uneNote:
                            if uneNote.split(':')[0].strip()==cle:
                                ticket.update({cle:uneNote.split(':')[1]})

            allData = pd.concat([allData,pd.DataFrame(pd.Series(ticket)).T])
        
        return allData

    def BibtexFindCles(self,filename):
        with open(filename) as bibtex_file:
            bibtex_str = bibtex_file.read()
            
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        bib_database = bibtexparser.loads(bibtex_str,parser=parser)
        lesCles = []
        for entry in bib_database.entries:
            if 'annote' in entry.keys():
                for uneNote in entry['annote'].split('\n') :
                    if ":" in uneNote:
                            lesCles.append(uneNote.split(":")[0].strip())
        return list(set(lesCles))
        


if __name__ == "__main__":
    adr = os.path.dirname(os.path.realpath(__file__)) + \
    os.sep + "example_data" + os.sep
    filenameBib = "simu.bib"
    to = ArticleTools()
    
    #%%
    # ---------------------
    # Récupération du fichier .ris
    allData = pd.DataFrame()
    lesCles = ["material","melting","solidification","type_MCP","lh","cond_therm","density","country","weather","software","method","scale","model","Num_vs_Expe","nb_citing","comment","lu_par"]
    allData = to.ParserBibtexWithNote(adr+filenameBib,lesCles)
    allData = allData.sort_values(by=['year'], ascending=False)
    allData.to_csv(adr + 'simu.csv',index=False)   

    #%%
    # ---------------------
    # Récupération des lignes dont la méthode est enthalpique
    enthalpyData = allData[(allData["model"].str.contains("enthalpy", na = False) & allData["method"].str.contains("FD", na = False))]

    # %%
    # ---------------------
    # Ecriture du tableau .tex
    allData[["id","year","country","software","method","model"]].to_latex(adr + "table.tex", index = False, escape = False)
    allData[["id","year","country","software","method","model"]].to_csv(adr + "table.csv", index = False)