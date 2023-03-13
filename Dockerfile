# Use the official Miniconda3 image as the base image
FROM continuumio/miniconda3

# Copy the current directory contents into the container at /app
# COPY . .

# # Create a new Conda environment with Python 3
RUN conda create -n torch python=3.10

# # Activate the Conda environment
SHELL ["conda", "run", "-n", "torch", "/bin/bash", "-c"]

# # Install PyTorch and torchvision
RUN conda install numpy -y

RUN git clone https://github.com/apatankar22/hier-neural-proc.git

# Set the working directory to /app
WORKDIR /hier-neural-proc

# # Set the default command to run when the container starts
ENTRYPOINT [ "conda", "run", "-n", "torch"]
WORKDIR /hier-neural-proc/src
CMD ["python", "run.py", "test"]
# CMD ["conda", "run", "-n", "torch", "python", "main.py"]
