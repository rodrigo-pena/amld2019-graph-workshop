# Learning and Processing over Networks

A workshop presented by [Michaël Defferrard](http://deff.ch) and [Rodrigo Pena](https://rodrigo-pena.github.io) at the [Applied Machine Learning Days](https://www.appliedmldays.org) in January 2019.

* Conference page: <https://www.appliedmldays.org/workshops/learning-and-processing-over-networks>
* Slides: <https://doi.org/10.5281/zenodo.2551081>

We suggest you follow the [installation guide](#installation) to setup your own computer.
If you don't succeed, you can work in the cloud using [binder].

## Description

The workshop will introduce the participants to graphs/networks, and provide pointers on how to deal with information defined on such domains.

Participants will be able to see two kinds of graphs: (i) those that are discrete representations of continuous domains, and (ii) those that model relations between entities.
Examples of data supported on the networks of the first category are temperature/rain/snow measurements over the Earth, or wind drag over a 3D wing model, or yet category labels (e.g., "land", "buildings", "cars", "people") over a 3D point cloud acquired for autonomous vehicles, land surveys, or indoor mapping.
The graphs of the second category include social networks (representing relations between people, and including data about them), the internet (seen through hyperlinks between websites), telecommunication networks (e.g., examining the number of packets per second traveling via the fibers connecting routers), interaction networks (user-product, product-patent, user-user, etc.), road systems, energy networks, and even molecules.

Indeed, networks are ubiquitous in the real world, and, today, data is plenty. In an abstract framework, once the graph and data are defined, the same analysis tools can be used to comprehend that information across various applications. This framework and its tools are the ones we will work with during this workshop. The proposed processing pipeline is versatile and can be fitted to all the examples above, and many more.

The key topics orbiting the theme of this workshop are Network Science, Spectral Graph Theory, Graph Signal Processing, and Machine Learning. After getting acquainted with the basics, participants will choose an application on which to work from a list based on some of the applications mentioned in the previous paragraphs.

**Outcome**

Participants will learn how to identify network data, how to deal with it, and what can be learned from it. They will know the basics of information processing over networks, and how to devise a machine learning system based on network data. Finally, the hands-on experience will give them the confidence to apply those tools in practice, in applications of their choice.

**Prerequisites**

* python programming
* basic linear algebra
* no prior knowledge about networks is necessary

## Content

This repository contains notebooks for you to practice the presented concepts.
They are meant to be worked on while following the slides.
The workshop has been prepared as a sequence of presentations and practical sessions.

The repository is made of three branches.
The `master` branch contains the notebooks with instructions and questions for you to follow and answer.
The `solutions` branch adds solutions.
The `outputs` branch contains an executed version of the `solutions` notebooks.
We recommend that you work from the `master` branch, and consult the solutions from the below links.

1. [Graph and network basics][basics]
1. [Network science: basic network properties][properties]
1. [Spectral methods: Laplacian eigenmaps and spectral clustering][spectral]
1. [Spectral representation and filtering][filters]

[basics]: https://nbviewer.jupyter.org/github/rodrigo-pena/amld2019-graph-workshop/blob/outputs/notebooks/01_basics.ipynb
[properties]: https://nbviewer.jupyter.org/github/rodrigo-pena/amld2019-graph-workshop/blob/outputs/notebooks/02_properties.ipynb
[spectral]: https://nbviewer.jupyter.org/github/rodrigo-pena/amld2019-graph-workshop/blob/outputs/notebooks/03_spectral.ipynb
[filters]: https://nbviewer.jupyter.org/github/rodrigo-pena/amld2019-graph-workshop/blob/outputs/notebooks/04_filters.ipynb

## Installation

[![Binder](https://mybinder.org/badge.svg)][binder]
&nbsp; Click the binder badge to play with the notebooks from your browser without installing anything.

[binder]: https://mybinder.org/v2/gh/rodrigo-pena/amld2019-graph-workshop/master?urlpath=lab

For a local installation, you will need [git], [python >= 3.6][python], [jupyter], and packages from the [python scientific stack][scipy].
If you don't know how to install those on your platform, we recommend to install [miniconda], a distribution of the [conda] package and environment manager. Please follow the below instructions to install it and create an environment for the course.

1. Download the python 3.x installer for Windows, macOS, or Linux from <https://conda.io/miniconda.html> and install with default settings.
   Skip this step if you have conda already installed (from [miniconda] or [anaconda]).
   Linux users may prefer to use their package manager.
   * Windows: Double-click on the `.exe` file.
   * macOS: Run `bash Miniconda3-latest-MacOSX-x86_64.sh` in your terminal.
   * Linux: Run `bash Miniconda3-latest-Linux-x86_64.sh` in your terminal.
1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Install git with `conda install git`.
1. Download this repository by running `git clone https://github.com/rodrigo-pena/amld2019-graph-workshop`.
1. Create an environment with `conda create --name amld2019_graph_workshop`.
1. Activate the environment with `conda activate amld2019_graph_workshop`
   (or `activate amld2019_graph_workshop`, or `source activate amld2019_graph_workshop`).
1. Within this environment, install packages by running `conda install -c conda-forge python=3.6 jupyterlab geos proj4 libspatialindex`, then `pip install -r requirements.txt`.

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate amld2019_graph_workshop`
   (or `activate amld2019_graph_workshop`, or `source activate amld2019_graph_workshop`).
1. Start Jupyter with `jupyter lab`.
   The command should open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

Run the `test_install.ipynb` Jupyter notebook to make sure that the main packages can at least be imported.

If you notice errors of the type 'There is no package called `osmnx`' or 'There is no package called `cartopy`', it is because there was an issue while installing them from the `requirements.txt` file.
A possible solution is to install those packages with conda, by running `conda install -c conda-forge osmnx cartopy` in the terminal, from within the `amld2019_graph_workshop` environment.

[git]: https://git-scm.com
[python]: https://www.python.org
[jupyter]: https://jupyter.org/
[scipy]: https://www.scipy.org
[conda]: https://conda.io
[miniconda]: https://conda.io/miniconda.html
[anaconda]: https://anaconda.org

## Acknowledgments

The content of the workshop is inspired by the following resources:

* The EPFL course "A Network Tour of Data Science", editions [2017][ntds2017] and [2018][ntds2018].
* [Voting patterns in the Swiss National Council][swiss_council], an NTDS'18 student project.
* [Finding Continents from a Flight Routes Network][flight_routes], another NTDS'18 student project.
* The [tutorials from the PyGSP documentation][pygsp_tutorials].
* The [practical session][graphsip] of the GraphSIP summer school.

[ntds2017]: https://github.com/mdeff/ntds_2017
[ntds2018]: https://github.com/mdeff/ntds_2018
[swiss_council]: https://github.com/nikolaiorgland/conseil_national
[flight_routes]: https://github.com/franckdess/NTDS_Project
[pygsp_tutorials]: https://pygsp.readthedocs.io/en/stable/tutorials
[graphsip]: https://github.com/mdeff/pygsp_tutorial_graphsip

## License

The content is released under the terms of the [MIT License](LICENSE.txt).
