on pourrait séparer 2 progs différents:
mpirun -np1 gui.py : -np 4 grid.py

def app
    def draw (grid...)

mpi.reduce

il vaut mieux couper ds le sens de construction du tableau pr calculs pas trop complexes

granularité,latence, à minimiser 
(gros échanges, peu d'échanges)

recouvrement sur 1 colonne = colonne fantome
tore => cellules fantomes sur bord aussi

attention synchro, comm globale permet la synchro

lifegame : memory bound -> svt : speedup max = 2