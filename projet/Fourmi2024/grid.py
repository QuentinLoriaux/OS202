import numpy as np
import myPheromone
import myAnts
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

workers = comm.Split(1)
wRank = workers.Get_rank()
wSize = workers.Get_size()


if __name__ == "__main__":
    import sys
    import time
    
    #receive parameters
    # size_laby, max_life, alpha, beta = comm.recv(source = 0)
    # size_laby, max_life, alpha, beta  = None, None, None, None
    # data = None
    size_laby, max_life, alpha, beta =comm.bcast(None, root=0)
    # size_laby, max_life, alpha, beta = data
    # print(size_laby)
    
    nb_ants = size_laby[0]*size_laby[1]//4
    nb_ants //= wSize
    # print(nb_ants)
    pos_food = size_laby[0]-1, size_laby[1]-1
    pos_nest = 0, 0

    maze = comm.bcast(None, root = 0)
    ants = myAnts.Colony(nb_ants, pos_nest, max_life)
    # unloaded_ants = np.array(range(nb_ants))
    pheromones = myPheromone.Pheromon(size_laby, pos_food, alpha, beta)
    
    food_counter = 0
    playing = True
    
    print(wRank)


    
    

    
    while playing:

            
        #compute
        deb = time.time()
        food_counter = ants.advance(maze, pos_food, pos_nest, pheromones, food_counter)
        pheromones.do_evaporation(pos_food)
        end = time.time()

        #communication
        comm.gather((ants, food_counter), root = 0)
        comm.reduce(pheromones.pheromon, op = MPI.SUM, root = 0)
        # comm.Reduce([pherom,MPI.DOUBLE], [pherom,MPI.DOUBLE], MPI.SUM, root = 0)
        # comm.send((pherom.pheromon, ants, food_counter), dest = 0)
        playing = comm.bcast(None, root = 0)


        
        print(f"FPS : {1./(end-deb):6.2f}, nourriture : {food_counter:7d}\n", end='\r')
