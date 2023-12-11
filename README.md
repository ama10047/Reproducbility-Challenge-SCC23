# Reproducbility-Challenge-SCC23
The Reproducibility Challenge is based on SC22 paper "Symmetric Block-Cyclic Distribution: Fewer Communications Leads to Faster Dense Cholesky Factorization". In this paper, the authors are interested in the Cholesky factorization of large dense matrices performed in parallel in a distributed manner. Inspired by recent progress on asymptotic lower bounds on the total number of communications required to perform this operation, they present an original data distribution, Symmetric Block Cyclic (SBC), as an alternative to the standard 2D Block Cyclic (2DBC) distribution implemented in ScaLAPACK. It is designed to take advantage of the symmetry of the matrix to reduce inter-process communications. SBC is implemented within the paradigm of task-based runtime systems using the dense linear algebra library Chameleon associated with the StarPU runtime system. Experiments were carried out on the experimental platform PlaFRIM using homogeneous CPU-only nodes. The factorization of several synthetic test case matrices demonstrate that using the SBC distribution actually reduces the total volume of inter-process communication by a factor of √2, compared to the standard 2DBC distribution, as predicted by the theoretical analysis. The results clearly show that using SBC allows better performance and scalability than with 2DBC distribution in all tested configurations. 

Now, inorder to run the codes and check for the results and plot graphs following steps are required:

1. Install chameleon on the cluster. The install details are given in: https://solverstack.gitlabpages.inria.fr/chameleon/#download
2. Load the modules according th your cluster setup, make sure all parameters are inherent.
3. Save the 2DBC codes as an .sh extension and run them with bash command.
4. The results are saved in data(size).txt files.
5. Then run for all the modules required.
6. Next step is to run the SBC code and for parralelization run the main sbatch file as in sbatch command.
7. All test results would be saved in the appropriate directory and will be able to compute and view them later.
8. Last step is to use the graphing tools or softwares to compute appropriate graphs accordingly.
9. The test is to reproduce tests ran in the main paper: https://inria.hal.science/hal-03768910/document
10. At last deduce the observations and confirm the high end performance of the SBC code vs 2DBC.
