# TD n°3 - parallélisation du Bucket Sort

*Ce TD peut être réalisé au choix, en C++ ou en Python*

Implémenter l'algorithme "bucket sort" tel que décrit sur les deux dernières planches du cours n°3 :

- le process 0 génère un tableau de nombres arbitraires,
- il les dispatch aux autres process,
- tous les process participent au tri en parallèle,
- le tableau trié est rassemblé sur le process 0.


se débrouiller pour que chaque processus ait son sous paquet de données
scatter en listes égales
calculer min/max pour chaque sous liste egale
réduction min/max

dans un bucket :
plusieurs sous buckets

d'abord : décider buckets
on peut tt faire sur le processus 0 ou dispatcher