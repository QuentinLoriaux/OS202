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

# Compte Rendu

Quentin Loriaux - Samy Vincent

## Analyse a priori

## Notre configuration

![myConfig.png](img/myConfig.png "using lstopo")

## trucs à repiquer

```
#! /bin/bash

echo "# cpus   time(s)"

# for smp in 1 2 4 8 $(seq 12 4 96) ; do
for smp in $(seq 1 200) ; do
    /bin/echo -e -n "$smp \t "
    OMP_NUM_THREADS=$smp ./Mandelbrot-openmp.exe |cut -d ' ' -f 6
    # OMP_NUM_THREADS=$smp taskset --cpu-list 0-${smp} ./Mandelbrot.exe |cut -d ' ' -f 6
done
```

