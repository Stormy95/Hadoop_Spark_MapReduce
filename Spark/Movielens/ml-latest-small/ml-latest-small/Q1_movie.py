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
    
    tableau_ratings = sc.textFile(sys.argv[1]).map(lambda line: line.split(',')) # userId  movieId	rating
    tableau_movies = sc.textFile(sys.argv[2]).map(lambda line: line.split(','))

    paires_ratings = tableau_ratings.map(lambda champs: (champs[1],champs[2])) # movieId rating 
    paires_movies = tableau_movies.map(lambda champs: (champs[0],champs[1])) # movieId title

    paires_ratings = paires_ratings.filter(lambda duet: duet[1]!='' and duet[1]!='rating') # on retire les valeurs manquantes et le titre
    paires_movies = paires_movies.filter(lambda duet: duet[0]!='movieId') # on retire le titre

    paires_ratings = paires_ratings.map(lambda champs: (champs[0],float(champs[1]))) # movieId rating 
    
    paires_ratings_sum= paires_ratings.reduceByKey(lambda v1,v2 : v1+v2) # on  somme les notes de tous les films

    paires_ratings_count = tableau_ratings.map(lambda champs: (champs[1],1)) # movieId  1
    paires_ratings_count= paires_ratings_count.reduceByKey(lambda v1,v2 : v1+v2) # on  compte le nombre de fois où chaque film est noté

    threshold = float(sys.argv[3])
    paires_ratings_count = paires_ratings_count.filter(lambda pair: pair[1]>threshold) # on donne un nombre minimale de notation de film

    classement = paires_ratings_sum.join(paires_ratings_count) # movie id, (sum des ratings, count des ratings)
    classement = classement.map(lambda champs: (champs[1][0]/champs[1][1],(champs[0],champs[1][0],champs[1][1]))) # rapport sum/count,(movie id, sum des ratings, count des ratings)
    classement = classement.sortByKey(ascending=False) # classement décroissant par rapport sum/count
    classement_join = classement.map(lambda champs: (champs[1][0],(champs[0],champs[1][1],champs[1][2]))) # movie id,  (rapport sum/count,sum des ratings, count des ratings)

    classement_final = classement_join.join(paires_movies) # on join les 2 dataframes pour obtenir le nom des movies
    
    classement_final.saveAsTextFile("classement")

	# Arret du contexte Spark
    sc.stop()

