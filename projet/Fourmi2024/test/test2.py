from mpi4py import MPI
import tkinter as tk

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if rank == 0:
        # Code for GUI setup
        root = tk.Tk()
        # GUI setup code here
        data_to_broadcast = "Hello from Rank 0"
    else:
        data_to_broadcast = None

    # Broadcast data from rank 0 to all other ranks
    data_to_broadcast = comm.bcast(data_to_broadcast, root=0)
    
    # if rank != 0:
    #     print(f"Rank {rank} received: {data_to_broadcast}")

    if rank == 0:
        root.mainloop()

if __name__ == "__main__":
    main()