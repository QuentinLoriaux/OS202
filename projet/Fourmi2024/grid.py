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
    
    #receive parameters
    size_laby, max_life, alpha, beta = comm.recv(source = 0)
    
    
    
    nb_ants = size_laby[0]*size_laby[1]//4
    pos_food = size_laby[0]-1, size_laby[1]-1
    pos_nest = 0, 0

    maze = comm.recv(source = 0)
    ants = myAnts.Colony(nb_ants, pos_nest, max_life)
    unloaded_ants = np.array(range(nb_ants))
    pherom = myPheromone.Pheromon(size_laby, pos_food, alpha, beta)
    
    food_counter = 0
    playing = True
    


    
    

    
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

