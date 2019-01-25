# Learning and Processing over Networks

A workshop presented by [Michaël Defferrard](http://deff.ch) and [Rodrigo Pena](https://rodrigo-pena.github.io) at the [Applied Machine Learning Days](https://www.appliedmldays.org) in January 2019.

* Conference page: <https://www.appliedmldays.org/workshops/learning-and-processing-over-networks>
* Slides: <https://doi.org/10.5281/zenodo.???>

## Content

Below are links to the executed version of the notebooks contained in this repository:

## Installation

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
   (or `activate pygsp_tutorial_graphsip`, or `source activate amld2019_graph_workshop`).
1. Within this environment, install packages by running `conda install -c conda-forge python=3.6 jupyterlab`, then `pip install -r requirements.txt`.

Every time you want to work, do the following:

1. Open a terminal. Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate amld2019_graph_workshop`
   (or `activate pygsp_tutorial_graphsip`, or `source activate amld2019_graph_workshop`).
1. Start Jupyter with `jupyter lab`.
   The command should open a new tab in your web browser.
1. Edit and run the notebooks from your browser.

Run the `test_install.ipynb` Jupyter notebook to make sure that the main packages can at least be imported.

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
* The [tutorials from the PyGSP documentation][pygsp_tutorials].
* The [practical session][graphsip] of the GraphSIP summer school.

[ntds2017]: https://github.com/mdeff/ntds_2017
[ntds2018]: https://github.com/mdeff/ntds_2018
[swiss_council]: https://github.com/nikolaiorgland/conseil_national
[pygsp_tutorials]: https://pygsp.readthedocs.io/en/stable/tutorials
[graphsip]: https://github.com/mdeff/pygsp_tutorial_graphsip

## License

The content is released under the terms of the [MIT License](LICENSE.txt).
