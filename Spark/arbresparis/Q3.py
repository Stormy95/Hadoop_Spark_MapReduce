##!/usr/bin/python

# d’afficher toutes les espèces d’arbre, triées par genre.

#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from pyspark import SparkContext

if __name__ == "__main__":

    # Creation d un contexte Spark
    sc = SparkContext(appName="Spark Count")
    sc.setLogLevel("ERROR") # Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
    
    tableau = sc.textFile(sys.argv[1]).map(lambda line: line.split(';'))
   
    paires = tableau.map(lambda champs: (champs[2],champs[3]))  # genre, espèce

    pairesok1 = paires.filter(lambda duet: duet[0]!='' or duet[1]!='') #on retire les valeurs manquantes



    pairesok2 = pairesok1.distinct() #on retire les doublons

    classement = pairesok2.sortByKey() # classement croissant (alphabetique)

    classement.saveAsTextFile("classement")

	# Arret du contexte Spark
    sc.stop()



