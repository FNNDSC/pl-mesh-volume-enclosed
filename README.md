# pl-pyvista-volume

[![Version](https://img.shields.io/docker/v/fnndsc/pl-pyvista-volume?sort=semver)](https://hub.docker.com/r/fnndsc/pl-pyvista-volume)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-pyvista-volume)](https://github.com/FNNDSC/pl-pyvista-volume/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-pyvista-volume/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-pyvista-volume/actions/workflows/ci.yml)

`pl-pyvista-volume` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which calculates the volume enclosed by a polygonal mesh. It accepts an input directory containing MNI .obj surface files, and writes outputs to both stdout and text files in an output directory.

[PyVista](https://github.com/pyvista/pyvista) is used for calculating volume from a polygonal mesh.

## Installation

`pl-pyvista-volume` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://raw.githubusercontent.com/FNNDSC/ChRIS_store_ui/963938c241636e4c3dc4753ee1327f56cb82d8b5/src/assets/public/badges/light.svg)](https://chrisstore.co/plugin/pl-pyvista-volume)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-pyvista-volume` as a container:

```shell
apptainer exec docker://fnndsc/pl-pyvista-volume surfvol input/ output/
```

To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-pyvista-volume surfvol --help
```

See [examples](./examples) for sample data.

## Local Installation

For development, use `pip` to install the package locally.

```shell
python -m venv venv
source venv/bin/activate
pip install -e .
```

### Testing

```shell
pytest
```

## Notes

### Multiprocessing

`vtk` and `pyvista` require multiprocessing (instead of multithreading) for concurrency. On 8 cores:

multiprocessing:

    real    0m38.632s
    user    2m31.680s
    sys     0m7.660s

multithreading:

    real    2m43.133s
    user    2m28.311s
    sys     0m5.364s
