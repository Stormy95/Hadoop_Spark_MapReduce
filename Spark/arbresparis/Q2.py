##!/usr/bin/python

# Afficher les coordonnées GPS des arbres de plus grandes circonférences pour chaque arrondissement de la ville de Paris.


#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
from pyspark import SparkContext

if __name__ == "__main__":

	# Creation d un contexte Spark
    sc = SparkContext(appName="Spark Count")
    sc.setLogLevel("ERROR") # Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
    
    tableau = sc.textFile(sys.argv[1]).map(lambda line: line.split(';'))
   
    paires = tableau.map(lambda champs: (champs[7],(float(champs[11]),champs[18]))) # arrondissement, gps, circonference

    pairesok1 = paires.filter(lambda duet: duet[1][0]!='') #on retire les valeurs manquantes de circonference

    pairesok2=pairesok1.reduceByKey(lambda v1,v2 : max(v1,v2))

    classement = pairesok2.sortByKey() # classement croissant (alphabetique)

    classement.saveAsTextFile("classement")

	# Arret du contexte Spark
    sc.stop()

