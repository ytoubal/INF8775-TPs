for i in $(seq 30 5 55)
do
    echo "Taille ${i}"
    for algo in "glouton" "branch_bound" "tabou"
    do
        echo "Algo ${algo}"
        for j in $(seq 10)
        do
            ./tp.sh -a ${algo} -e instances/${i}/ex_${i}_${j} -p | py script.py
        done
    done
done