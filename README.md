# Unveiling the Business of Data: Data on Data Brokers

## Project Goal
Data brokers buy and aggregate billions of data elements on individuals, selling this sensitive data—often without explicit consent—to companies that target demographic subgroups with advertisements and addictive online products. It is unclear what information data brokers collect, where data is transferred, and how much control consumers can actually assert over their personal data. While some states have taken steps to create centralized, state-wide data broker registries, compliance issues persist, as registries are not easily accessible and few states provide their residents with real control over their data. For this project, we would like to define what data brokers are, identify the key actors involved in the data economy, and address this lack of transparency in the data broker market. We hope to shed light on this industry and answer questions about data broker practices and the difficulty of deleting personal data. Ultimately, we aim to evaluate and identify gaps in existing law and privacy practices.

## Repository Structure
```
.
├── README.md               # Project documentation
├── Gemfile                 # Ruby dependencies for Jekyll
├── .gitignore              # Git ignore rules
├── data/                   # Data files and datasets
│   ├── README.md           # Data documentation
│   ├── cleaned_data/       # Processed datasets
│   └── raw_data/           # Original datasets
├── data_utils/             # Data processing utilities (Python)
│   ├── __init__.py
│   └── data_cleaner.py     # Data cleaning functions
├── notebooks/              # Jupyter notebooks for analysis
│   ├── clearinghouse_analysis.ipynb
│   ├── info-extraction.ipynb
│   └── privacy-policy-analysis.ipynb
└── docs/                   # Contains the Jekyll site for GitHub Pages
    ├── _config.yml         # Jekyll site configuration
    ├── index.md            # Site homepage
    ├── _posts/             # Blog post content
    ├── project_report_1.md
    └── project_report_2.md
```

## Website
This project includes a static website built with Jekyll, hosted on GitHub Pages. The content for the site is located in the `/docs` directory.

### How to Run Locally
To preview the website on your local machine, you will need Ruby and Bundler installed.

1.  **Install Dependencies:**
    Navigate to the project's root directory and run Bundler to install the gems specified in the `Gemfile`.
    ```bash
    bundle install
    ```

2.  **Serve the Site:**
    Run the Jekyll server. The `--source` flag tells Jekyll to look for the site content in the `docs` directory.
    ```bash
    bundle exec jekyll serve --source docs
    ```

3.  **View the Site:**
    Open your web browser and go to `http://localhost:4000`.

##  Group Members
| Name | GitHub Handle |
| :--- | :--- |
| Minjae Joh | @mjayjoh |
| Michelle Du | @michellecdu |
| Ornella Ndatabaye | @ornella-1 |