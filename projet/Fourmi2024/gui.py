import numpy as np
import myMaze
import myAnts
import pygame as pg

from mpi4py import MPI

# import os
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"

comm = MPI.COMM_WORLD.Dup()
rank = comm.Get_rank()
size = comm.Get_size()


def loadAssets():
    #  Load patterns for maze display :
    global cases_img
    cases_img = []
    img = pg.image.load("img/cases.png").convert_alpha()
    for i in range(0, 128, 8):
        cases_img.append(pg.Surface.subsurface(img, i, 0, 8, 8))

    # Load sprites for ants display :
    global sprites 
    sprites = []
    img = pg.image.load("img/ants.png").convert_alpha()
    for i in range(0, 32, 8):
        sprites.append(pg.Surface.subsurface(img, i, 0, 8, 8))


def displayMaze(maze):
    """
    Create a picture of the maze :
    """
    maze_img = pg.Surface((8*maze.shape[1], 8*maze.shape[0]), flags=pg.SRCALPHA)
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            maze_img.blit(cases_img[maze[i, j]], (j*8, i*8))

    return maze_img


def displayAnts(ants, screen):
        [screen.blit(sprites[ants.directions[i]], (8*ants.historic_path[i, ants.age[i], 1], 8*ants.historic_path[i, ants.age[i], 0])) for i in range(ants.directions.shape[0])]



def getColor(pheromon, i: int, j: int):
    val = max(min(pheromon[i, j], 1), 0)
    return [255*(val > 1.E-16), 255*val, 128.]

def displayPheromon(pheromon, screen):
    [[screen.fill(getColor(pheromon, i, j), (8*(j-1), 8*(i-1), 8, 8)) for j in range(1, pheromon.shape[1]-1)] for i in range(1, pheromon.shape[0]-1)]






if __name__ == "__main__":
    import sys
    import time
    
    pg.init()


    #treat inputs
    size_laby = 25, 25
    if len(sys.argv) > 2:
        size_laby = int(sys.argv[1]),int(sys.argv[2])

    max_life = 500
    if len(sys.argv) > 3:
        max_life = int(sys.argv[3])
    
    alpha = 0.9
    if len(sys.argv) > 4:
        alpha = float(sys.argv[4])

    beta  = 0.99
    if len(sys.argv) > 5:
        beta = float(sys.argv[5])

    #send parameters
    for k in range(1, size) :
        comm.send((size_laby, max_life, alpha, beta), dest = k)
    
    # screen init
    resolution = size_laby[1]*8, size_laby[0]*8
    screen = pg.display.set_mode(resolution)

    # load assets
    loadAssets()

    # maze init
    a_maze = myMaze.Maze(size_laby, 12345)  
    comm.send(a_maze.maze, dest = 1)
    mazeImg = displayMaze(a_maze.maze)# Le labyrinthe ne change pas


    playing = True
    snapshop_taken = False
           

    
    while playing:


        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                playing = False
                
        #communication
        pherom, ants, food_counter = comm.recv(source = 1)
        comm.send(playing, dest = 1)

        #display
        displayPheromon(pherom,screen)
        screen.blit(mazeImg, (0, 0))
        displayAnts(ants, screen)
        pg.display.update()
        # pg.time.wait(200)

        #save img
        if food_counter == 1 and not snapshop_taken:
            pg.image.save(screen, "img/MyFirstFood.png")
            snapshop_taken = True
        
        if not playing :
            pg.quit()
            
            


#mpirun -np 1 python3 gui.py : -np 1 python3 grid.py