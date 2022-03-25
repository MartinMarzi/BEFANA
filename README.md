# BEFANA: A Tool for Biodiversity-Ecosystem Functioning Assessment by Network Analysis

Interactive Jupyter notebooks and python code for soil food web visualization and analysis. Please refer to our paper in pre-print for further details: https://arxiv.org/abs/2203.11687.

## Tool structure:
BEFANA consists of these jupyter notebooks: 

Part 1: Preparing the environment and loading the data
Part 2: Network construction, editing and visualization
Part 3: Network analysis
Part 4: Modeling with experimental data
Part 5: Machine learning on graphs

## How to use

### Docker

The notebooks work best in a local installation containing Jupyter lab and other required packages. If you prefer docker or if you experience difficulties running the notebooks on your host operating system, you can try using the provided `docker-compose.yml file` as follows:

```bash
git clone git@github.com:vpodpecan/representation_learning.git
cd representation_learning
docker-compose up
```

When the container is up and running it will return a link to the Jupyter environment such as `http://127.0.0.1:8888/?token=159090399d58b41041bfc812cf2bf5aa1779fb54a6170005`. There you can open and run the provided notebooks.

### Local installation
#### Requirements

- python 3.8+ 
- jupyterlab

In addition, each notebook has its own requirements which are installed when the notebook is executed for the first time.

#### Preparing the environment

1. Create and activate a virtual environment.

    - Linux
      ```bash
      python3 -m venv myEnv
      source myEnv/bin/activate
      ```
  
    - Windows
      ```bash
      python3 -m venv myEnv
      myEnv\Scripts\activate
      ```
      
2. Clone the repository
    ```bash
    git clone https://github.com/vpodpecan/representation_learning.git
    ```

3. Install and run jupyterlab. The following commands install jupyterlab and run it.
    ```bash
    pip install jupyterlab
    cd representation_learning
    jupyter lab
    ```
4. Open the link in a web browser and select a notebook.

## How to contribute

Contributions are welcome! You are welcome to contribute corrections, new notebooks, examples, figures or any other material related to the contents of the book.

## License

The code and materials in this repository are licensed under the MIT license except where stated otherwise.
