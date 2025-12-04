# Analysis Notebooks

This directory contains Jupyter notebooks used for data exploration, analysis, and prototyping for the Data Broker Analysis project.

## Contents

- `clearinghouse_analysis.ipynb` - Analysis of data broker clearinghouse mechanisms
- `info-extraction.ipynb` - Privacy policy data extraction and processing workflows  
- `privacy-policy-analysis.ipynb` - Privacy policy analysis and comparison
- `survey-analysis.ipynb` - Analysis of survey data related to consumer awareness of data brokers
- `imgs` folder - Generated images from notebook analyses

## Usage

These notebooks are designed to be run in a Jupyter environment with the required dependencies installed (see `requirements.txt` in the project root).

To run the notebooks locally:

1. Install dependencies: `pip install -r requirements.txt`
2. Start Jupyter: `jupyter notebook`
3. Navigate to the notebook you want to run

## Data Sources

The notebooks work with data files located in the `../data/` directory. Make sure the data files are in place before running the analyses.

For the main application, see `../app.py` which incorporates the key analysis logic from these notebooks.