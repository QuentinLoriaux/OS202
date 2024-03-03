from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    # Receive broadcasted data from rank 0
    data_to_process = comm.bcast(None, root=0)

    if rank != 0:
        print(f"Rank {rank} received: {data_to_process}")

if __name__ == "__main__":
    main()