import numpy as np
import myPheromone
import myAnts
from mpi4py import MPI

import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

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
    size_laby, max_life, alpha, beta =comm.bcast(None, root=0)
    
    nb_ants = size_laby[0]*size_laby[1]//4
    nb_ants //= wSize
    pos_food = size_laby[0]-1, size_laby[1]-1
    pos_nest = 0, 0

    maze = comm.bcast(None, root = 0)
    ants = myAnts.Colony(nb_ants, pos_nest, max_life)
    # unloaded_ants = np.array(range(nb_ants))
    pheromones = myPheromone.Pheromon(size_laby, pos_food, alpha, beta)
    old_pheromones = myPheromone.Pheromon(size_laby, pos_food, alpha, beta)
    
    food_counter = 0
    playing = True
    shortestTime = 100000
    execution_times = []
    communication_times = []
    while playing:
        #compute
        deb = time.time()
        food_counter = ants.advance(maze, pos_food, pos_nest, pheromones, old_pheromones, food_counter)
        old_pheromones.do_evaporation(pos_food)
        end = time.time()

        execution_times.append(end - deb)

        #communication
        comm.barrier()
        deb = time.time()
        comm.gather((ants, food_counter), root = 0)
        copyPheromon = old_pheromones.pheromon.copy()
        comm.Reduce([copyPheromon,MPI.DOUBLE], None, MPI.SUM, root = 0)
        playing, pheromones.pheromon = comm.bcast(None, root = 0)
        end = time.time()
        communication_times.append(end - deb)
        
        # if wRank == 0:
        #     if (end-deb<shortestTime):
        #         shortestTime = end-deb
            # print(f"maxFPS worker 0: {1./shortestTime:6.2f}", end='\r')
                # sys.stdout.write("   time Worker 0 : " + str(shortestTime) + '\r')
                # sys.stdout.flush()
    
    average_time = sum(execution_times) / len(execution_times)
    print(average_time)
