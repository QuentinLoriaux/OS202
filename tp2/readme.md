### TD2

## 1. Interblocages

Un processus envoie à tous, tous les autres reçoivent.

Les 2 processus sont en réception : attendent un message
=> interblocage

Exemple du cours : le process 2 reçoit d'abord le message 1
et se trouve en blocage avec 0 car les 2 attendent reception.
Ordre d'arrivée des messages : imprévisible!
probabilité de blocage : intuitivement, 1/2

-> faire des schémas fléchés

## 2. Question cours

Selon la loi d'Amdhal, 10% d'execution pas en parallèle
=> speedup_max = 1/0.1 = 10

Environ 5 noeuds de calcul serait raisonnable car pour augmenter le speedup d'un facteur 2, il faudrait passer à plus de 20 coeurs.

1er cas :
S1 = 4 = n+(1-n)ts1

2e cas : (données x2 donc ts2+tp2=1 => ts2=1-2tp1= 2ts1-1)
S2 = 2(n+(1-n)ts1) -1 = 2S2-1 = 8-1 = 7
speedup max = 7

## 3. Mandelbrot

Sequentiel :
Temps du calcul de l'ensemble de Mandelbrot : 2.8319613933563232
Temps de constitution de l'image : 0.04209709167480469

variables globales/locales
fonction gather : réunit tout sur la destination
mpi4py.comm voir sur internet
Recv : pour numpy
recv : général

Speedup calculés par rapport au calcul du mandelbrot

Parallélisation:
3 processus :
Temps du calcul de l'ensemble de Mandelbrot : 1.4292783737182617
Temps de constitution de l'image : 0.05841851234436035 
Speedup = 1.98
4 processus :
Temps du calcul de l'ensemble de Mandelbrot : 1.067394495010376
Temps de constitution de l'image : 0.04744124412536621
Speedup = 2.65
5 processus :
Temps du calcul de l'ensemble de Mandelbrot : 0.8112199306488037
Temps de constitution de l'image : 0.051143646240234375
Speedup = 3.49
6 processus :
Temps du calcul de l'ensemble de Mandelbrot : 0.6763904094696045
Temps de constitution de l'image : 0.049382925033569336
Speedup = 4.19

Interprétation : 
L'accélération est linéaire en le nombre de processus.
Cela correspond à la loi de Gustaffon (le nombre de données à traiter est fixe)

Maître esclave :
4 processus :
Temps du calcul de l'ensemble de Mandelbrot : 0.9760355949401855
Temps de constitution de l'image : 0.03694558143615723
Speedup = 2.901
5 processus :
Temps du calcul de l'ensemble de Mandelbrot : 0.777463436126709
Temps de constitution de l'image : 0.03929638862609863
Speedup = 3.645
6 processus :
Temps du calcul de l'ensemble de Mandelbrot : 0.6218395233154297
Temps de constitution de l'image : 0.037343740463256836
Speedup = 4.55

La méthode maître esclave est plus efficace.
Ici, on envoie successivement à chaque processus les lignes en faisant un cycle d'envoi/récupération => gain de temps car on construit la matrice numpy en même temps qu'on calcule

## Produit matrice-vecteur

S'il y a nbp tâches, on a Nloc = N/nbp