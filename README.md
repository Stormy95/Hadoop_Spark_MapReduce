# Hadoop_Spark_MapReduce

## MapReduce

Use of MRjob library to make map reduce requests (wordcount of dracula and analysis of purchases datasets) on Hadoop. 

## Spark

Use of pyspark to make spark requests (wordcount, analysis of a movie and rating datasets and arbresdeparis set) on Hadoop

## Liste of commands:

Send file to Docker :
docker cp PySpark_wc.py hadoop-master:/root/
(Then mkdir wordcount and then mv PySpark_wc.py ~/wordcount

Upload a file in docker :
docker cp wc1_mrjob.py hadoop-master:/root/wordcount

docker cp hadoop-master:/root/anagramme/words_100.txt C:/extract

Rendre scripts exécutables:
chmod +x wc1_mrjob.py

Caractères de saut de lignes:
dos2unix  wc1_mrjob.py

Hadoop map-reduce fonctionne avec le langage Java ; il faut donc utiliser une bibliothèque capable de transformer des instructions Python en instruction Java. C’est le rôle de cette bibliothèque hadoop-streaming-3.2.2.jar (on appelle cela un wrapper).
export STREAMINGJAR='/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar'

Run a Py file
hadoop jar $STREAMINGJAR -input input/dracula -output sortie  -mapper mapper.py -reducer reducer.py  -file mapper.py -file reducer.py

Run a python file
python wc1_mrjob.py -r hadoop hdfs:///user/root/input/dracula

Voir le dossier 'sortie':
hadoop fs -ls sortie/
Voir les dernières lignes :
hadoop fs -tail sortie/part-00000
Voir toutes les lignes :
hadoop fs -cat sortie/part-00000

Create a Folder and move a file in:
mkdir wordcount 
mv PySpark_wc.py ~/wordcount

Get the number of line of a file:
wc -l purchases.txt

cat purchases.txt | head -n 100 > purchases_extrait100.txt
