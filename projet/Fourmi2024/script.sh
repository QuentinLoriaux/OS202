echo "# cpus   time(s)"

for smp in $(seq 1 5) ; do
    /bin/echo -e -n "$smp \t "
    mpirun  -np 1 python3 gui.py 30 30 700 : -np $smp python3 grid.py
done
