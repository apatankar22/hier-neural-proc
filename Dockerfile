ARG BASE_CONTAINER=ucsdets/datahub-base-notebook:2022.3-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root

RUN apt update
RUN apt-get -y install aria2 nmap traceroute
RUN pip install --no-cache-dir babypandas geopandas matplotlib pandas numpy scipy scikit-learn seaborn torch torchvision dill pyyaml statsmodels


# Override command to disable running jupyter notebook at launch
CMD ["/bin/bash"]


