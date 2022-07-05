# PPNet
## Introduction
- **What is PPNet?**
PPNet is designed to uses genome information and analysis of phylogenetic profiles with binary similarity and distance measures to derive large-scale bacterial association networks of a single species.

## Installation
PPNet has the following dependencies:
* [prokka](https://github.com/tseemann/prokka)
* [roary](https://github.com/sanger-pathogens/Roary)
* Python(>=version 3.7)
* Python modules:
     - biopython
     - pyvis
     - numpy
     - scipy
     - statsmodels


- **Install with the source codes**
  - Download the source codes:
    ```bash
    git clone https://github.com/liyangjie/PPNet.git
    ```
  - Rename the main program and add the path to the environment variable:
    ```bash
    # Rename PPNet.py to PPNet
    mv PPNet/bin/ppnet.py PPNet/bin/ppnet
    # Give the scripts executable permission
    chmod +x PPNet/bin/*
    # Add the path to the environment variable
    echo export PATH="/Path/to/PPNet/bin:$PATH" >> ~/.bashrc
    source ~/.bashrc
    ```
  - Install the Python dependencies:
    ```bash
    pip install biopython pyvis numpy scipy statsmodels 
    ```
  - Install the external dependances either from source or from your packaging system:
    ```bash
    prokka roary
    ```
## Usage
``` bash
ppnet [Options]
```
```
Options:
      [-h] show this help message and exit
      [-i1] [Required] The path of input genomes
      [-i2] [Required] The path of phenotype (e.g., pathogenic or non-pathogenic) of all strains
      [-o] The path of output (Default "./PPNet_output")
      [-x] The suffix of genomes data (Default "fasta")
      [-c] number of CPUs to use
      [-a] [Required] Select the algorithm for calculating the correlation coefficient [1-81], or set 0 to use all algorithm.
      [-pt] What percentage of interactions will be visualized (Default "1")
```
## Examples
```
ppnet -i1 PATH/to/your/genomes/ -i2 group.csv -x fasta -c 4 -a 1
```
## Input
The genome file should be in fasta format and placed in the same path. The group.csv 


## Output
  - PPNet_output/HQ_data/* 
  - PPNet_output/NR_data/*
  - PPNet_output/Prokka_result/*
  - PPNet_output/Gff_file/*
  - PPNet_output/Roary_result/*
  - PPNet_output/Gene_Net.html 


    
