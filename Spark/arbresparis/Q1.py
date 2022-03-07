##!/usr/bin/python

# Afficher les coordonnées GPS, la taille et l’adresse de l’arbre le plus grand.

#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from pyspark import SparkContext

if __name__ == "__main__":

	# Creation d un contexte Spark
    sc = SparkContext(appName="Spark Count")
    sc.setLogLevel("ERROR") # Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
    
    tableau = sc.textFile(sys.argv[1]).map(lambda line: line.split(';'))
    
    paires = tableau.map(lambda champs: (float(champs[12]),(champs[18],champs[4]))) # taille, gps, adresse

    pairesok1 = paires.filter(lambda duet: duet[0]!='') #on retire les valeurs manquantes 

    classement = pairesok1.sortByKey(ascending=False) # classement décroissant

    classement.saveAsTextFile("classement")

	# Arret du contexte Spark
    sc.stop()

