<!---
![Image](images/IMAGE_TO_BE_INSERTED.png)
<p align="center"><em>IMAGE TITLE</em></p>
-->

# Abstract/Motivation

For simulations in different fields such as climatology and epidemiology, models can learn complex systems very accurately, with immense processing power and huge amounts of storage. 

Gaussian processes are models defining probability distributions over various functions. This leads to a data efficient and flexible solution; however, they are fairly computationally expensive. Neural processes improve on Gaussian processes by adapting the “priors” to data, and in turn improve model accuracy and reduce computation.  

Neural processes are designed for single-fidelity data, but through research in multi-fidelity neural processes, as shown by Wu et. al. \[1\], we achieve cheaper simulation costs and better predictions.

Active learning determines which training data to train on next via a reward function, further improving training convergence and stability. This project explores the possibilities of extending active learning on multi-fidelity neural processes to improve accuracy, training time, and simulation cost.

# Data
The data used for this project contains roughly 7000 high-dimensional complex simulations for the epidemiology modeling task at hand. The data stored is broken up into 109 different scenarios across different locations in the United States, Europe, and China, that is collected through macro and micro polls data. The low-fidelity data that is used contains an aggregation of data across 18 different age groups, while the high-fidelity data contains 85 different age groups.

# Models
Describe Models utilized here

# Methods
Describe methods used (specifically acquisition functions + others) here

# Results
Describe results + observations here

# Miscallenous

# References
\[1\] Dongxia Wu, Matteo Chinazzi, Alessandro Vespignani, Yi-An Ma, and Rose Yu. 2022. [Multi-fidelity Hierarchical Neural Processes](https://par.nsf.gov/servlets/purl/10347794). In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’22), August 14–18, 2022, Washington, DC, USA. ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3534678.3539364

\[2\] Wu, D., Niu, R., Chinazzi, M., Vespignani, A., Ma, Y. A., & Yu, R. (2021). [Deep Bayesian Active Learning for Accelerating Stochastic Simulation](https://arxiv.org/pdf/2106.02770.pdf). arXiv preprint arXiv:2106.02770. 

\[3\] Garnelo, M., Schwarz, J., Rosenbaum, D., Viola, F., Rezende, D. J., Eslami, S. M., & Teh, Y. W. (2018). [Neural processes](https://arxiv.org/pdf/1807.01622.pdf). arXiv preprint arXiv:1807.01622.
