FROM docker.io/fnndsc/conda:python3.10.6

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-pyvista-volume" \
      org.opencontainers.image.description="A ChRIS plugin to calculate the volume enclosed by MRI .obj surfaces using pyvista"

# install dependencies using conda for multi-arch support
RUN conda install -c conda-forge vtk=9.2.5 pyvista=0.37.0

# install Python package
WORKDIR /usr/local/src/pl-pyvista-volume
COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["surfvol", "--help"]
