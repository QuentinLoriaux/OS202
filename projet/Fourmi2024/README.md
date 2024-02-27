# Fourmi2024

markdown ou pdf
Faire le speedup, graphe, analyse
- analyse a priori (embarrassingly parallel ou pas? équilibré ou pas? memory bound ou cpu bound?)
- expliquer strat parallélisation
- code
- vérif code
- mesure analyse des perfs
- autocritique, ccl



affichage/calcul
paralléliser fourmis
pas à faire : paralléliser grille
    mais pistes réflexion dessus

import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MTK truc bidule_NUM_THREADS"] = "1"

