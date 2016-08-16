#CUCKOO SEARCH

Cuckoo Search (CS) is a meta-heuristic algorithm based on the breeding pattern of certain species of cuckoo birds. In our research, we have implemented CS for the NP-hard optimization problem, the Traveling Salesman Problem (TSP).  We initially followed the implementation given by Lang et al in their paper, “Discrete Cuckoo Search for the Traveling Salesman Problem.”  This was able to generate near-optimal solutions within 500 iterations, but not near-optimal solutions for fewer iterations.  The optimal solution was calculated using a Naïve brute force approach which has a complexity of (n!). In this case, we have 11 cities and so, the number of iterations to generate optimal solution by brute force is over 3 crores. In our research, we incorporated local search within the meta-heuristic algorithm and were able to generate near-optimal solutions for as low as 50 iterations.

The following results were tested for the input matrix in problem.py
##RESULTS

Algorithm|Output
--- | ---
Brute force | 253
Hill Climbing | 317



No. of iterations	| Original CS |	Modified Hybrid CS
--- | --- | ---
50	|296|	282
100	|292|	271
500	|256|	253
