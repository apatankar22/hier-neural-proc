<!---
![Image](images/IMAGE_TO_BE_INSERTED.png)
<p align="center"><em>IMAGE TITLE</em></p>
-->

# Abstract/Motivation

For simulations in different fields such as climatology and epidemiology, models can learn complex systems very accurately, with immense processing power and huge amounts of storage. 

Gaussian processes are models defining probability distributions over various functions. This leads to a data efficient and flexible solution; however, they are fairly computationally expensive. Neural processes improve on Gaussian processes by adapting the “priors” to data, and in turn improve model accuracy and reduce computation.  

Neural processes are designed for single-fidelity data, but through research in multi-fidelity neural processes, as seen [here](https://arxiv.org/pdf/2206.04872.pdf) we achieve cheaper simulation costs and better predictions.

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
