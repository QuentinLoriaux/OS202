import numpy as np
import myPheromone
import myAnts
from mpi4py import MPI

comm = MPI.COMM_WORLD.Dup()
rank = comm.Get_rank()
size = comm.Get_size() -1




if __name__ == "__main__":
    import sys
    import time
    
    size_laby = 25, 25
    if len(sys.argv) > 2:
        size_laby = int(sys.argv[1]),int(sys.argv[2])

    playing = True
    nb_ants = size_laby[0]*size_laby[1]//4
    pos_food = size_laby[0]-1, size_laby[1]-1
    pos_nest = 0, 0


    max_life = 500
    if len(sys.argv) > 3:
        max_life = int(sys.argv[3])
    
    alpha = 0.9
    beta  = 0.99
    if len(sys.argv) > 4:
        alpha = float(sys.argv[4])
    if len(sys.argv) > 5:
        beta = float(sys.argv[5])


    ants = myAnts.Colony(nb_ants, pos_nest, max_life)
    unloaded_ants = np.array(range(nb_ants))
    pherom = myPheromone.Pheromon(size_laby, pos_food, alpha, beta)
    food_counter = 0
    maze = comm.recv(source = 0)


    
    

    
    while playing:

            
        #compute
        deb = time.time()
        food_counter = ants.advance(maze, pos_food, pos_nest, pherom, food_counter)
        pherom.do_evaporation(pos_food)
        end = time.time()

        #communication
        comm.send((pherom.pheromon, ants, food_counter), dest = 0)
        playing = comm.recv(source = 0)


        
        print(f"FPS : {1./(end-deb):6.2f}, nourriture : {food_counter:7d}\n", end='\r')

