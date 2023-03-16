
# Capstone Project (DSC 180B): [Active Learning for Age-Stratified Epidemiology Modeling](http://apatankar22.github.io/hier-neural-proc/)
Authors: Amogh Patankar <br>
Mentors: Rose Yu, Yian Ma

## [SIR Neural Process and Gaussian Process Data](https://drive.google.com/drive/folders/1osXBkuDuzSmB8__2r3lLoOLHIXqju3G2)
SIR_GP: Save <code>nargp_data</code> and <code>sfgp_data</code> on the same level as <code>src</code>. 

SIR_NP: Save <code> mfnp_nested, nested, and nonnested </code> on the same level as <code>src/sir_np/ </code>. 

## Packages
Installed packages through pip. To replicate, run <code> pip install -r requirements.txt.</code>
Alternatively install along as you go, the Gaussian processes don't require all the same packages as the neural processes. 

## How to Run
For Gaussian Processes, simply change to <code>src/sir_gp</code> and run the two jupyter notebooks.
For Neural Processes, simply change to <code>src/sir_np/MA</code>, then go into the desired process and run train.py. This should train and also test + evaluate the model.
