# This is the Dockerfile to run Gammapy on Binder
#

FROM continuumio/miniconda3:4.5.4
MAINTAINER Gammapy developers <gammapy@googlegroups.com>

# compilers
RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip

# install dependencies - including the stable version of Gammapy
COPY binder.py tmp/
RUN curl -o tmp/environment.yml https://gammapy.org/download/install/gammapy-0.9-environment.yml

WORKDIR tmp/
RUN conda update conda
RUN conda install -q -y pyyaml
RUN python binder.py

# add gammapy user running the jupyter notebook process
ENV NB_USER gammapy
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# download tutorials and datasets
RUN gammapy download notebooks --out=${HOME}/gammapy-tutorials --release=0.9
RUN gammapy download datasets --out=${HOME}/gammapy-datasets

# RUN git clone https://github.com/gammapy/gammapy-extra.git ${HOME}/gammapy-extra
# RUN git clone https://github.com/gammapy/gammapy-cat.git ${HOME}/gammapy-cat
# RUN git clone https://github.com/gammapy/gammapy-fermi-lat-data.git ${HOME}/gammapy-fermi-lat-data

# setting ownerships
USER root
RUN chown -R gammapy:gammapy ${HOME}

# start JupyterLab server in tutorials dir
USER ${NB_USER}
WORKDIR ${HOME}/gammapy-tutorials/notebooks-0.9

# env vars used in tutorials
ENV GAMMAPY_DATA ${HOME}/${HOME}/gammapy-datasets

# ENV GAMMAPY_CAT ${HOME}/gammapy-cat
# ENV GAMMAPY_FERMI_LAT_DATA ${HOME}/gammapy-fermi-lat-data
