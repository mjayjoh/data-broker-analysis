# Unveiling the Business of Data: Data on Data Brokers

## Project Goal
Data brokers buy and aggregate billions of data elements on individuals, selling this sensitive data—often without explicit consent—to companies that target demographic subgroups with advertisements and addictive online products. It is unclear what information data brokers collect, where data is transferred, and how much control consumers can actually assert over their personal data. While some states have taken steps to create centralized, state-wide data broker registries, compliance issues persist, as registries are not easily accessible and few states provide their residents with real control over their data. For this project, we would like to define what data brokers are, identify the key actors involved in the data economy, and address this lack of transparency in the data broker market. We hope to shed light on this industry and answer questions about data broker practices and the difficulty of deleting personal data. Ultimately, we aim to evaluate and identify gaps in existing law and privacy practices.

## Repository Structure
```
.
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── _config.yml             # Jekyll site configuration
├── 404.html                # Custom 404 page
├── atom.xml                # Atom feed
├── CNAME                   # Custom domain configuration
├── index.md                # Site homepage content
├── LICENSE.md              # Project license
├── _includes/              # Jekyll includes
├── _layouts/               # Jekyll layouts
├── _plugins/               # Jekyll plugins
├── data/                   # Data files and datasets
│   ├── cleaned_data/       # Processed datasets
│   └── raw_data/           # Original datasets
├── data_utils/             # Data processing utilities (Python)
├── notebooks/              # Jupyter notebooks for analysis and visualization
│   └── imgs/               # Images used in notebooks
└── public/                 # Static assets for the Jekyll site
```

## Website
This project includes a static website built with Jekyll, hosted on GitHub Pages. The content for the site is located in the root directory.

The live website can be viewed at: [https://mjayjoh.github.io/data-broker-analysis/](https://mjayjoh.github.io/data-broker-analysis/)

## Replicating the Analysis
The analysis and visualizations in this project can be replicated by running the Jupyter notebooks located in the `notebooks/` directory. These notebooks contain the code for data exploration, analysis, and prototyping.

### How to Run the Notebooks
To run the notebooks on your local machine, you will need Python and the dependencies listed in `requirements.txt`.

1.  **Install Dependencies:**
    Navigate to the project's root directory and run pip to install the dependencies.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start Jupyter:**
    Run the Jupyter Notebook server from the project's root directory.
    ```bash
    jupyter notebook
    ```

3.  **View the Notebooks:**
    Open your web browser and navigate to the `notebooks/` directory to run the desired notebook.

### How to Run Locally
To preview the website on your local machine, you will need Ruby and the `jekyll` and `bundler` gems installed.

1.  **Install Dependencies (if you have a Gemfile):**
    If you have a `Gemfile`, navigate to the project's root directory and run Bundler to install the gems.
    ```bash
    bundle install
    ```
    *Note: This project currently does not use a Gemfile, so this step can be skipped.*

2.  **Serve the Site:**
    Run the Jekyll server from the root directory.
    ```bash
    bundle exec jekyll serve
    ```

3.  **View the Site:**
    Open your web browser and go to `http://localhost:4000`.

##  Group Members
| Name | GitHub Handle |
| :--- | :--- |
| Minjae Joh | @mjayjoh |
| Michelle Du | @michellecdu |
| Ornella Ndatabaye | @ornella-1 |