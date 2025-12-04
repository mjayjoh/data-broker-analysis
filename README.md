# Unveiling the Business of Data: Data on Data Brokers

## Project Goal
Data brokers buy and aggregate billions of data elements on individuals, selling this sensitive data—often without explicit consent—to companies that target demographic subgroups with advertisements and addictive online products. It is unclear what information data brokers collect, where data is transferred, and how much control consumers can actually assert over their personal data. While some states have taken steps to create centralized, state-wide data broker registries, compliance issues persist, as registries are not easily accessible and few states provide their residents with real control over their data. For this project, we would like to define what data brokers are, identify the key actors involved in the data economy, and address this lack of transparency in the data broker market. We hope to shed light on this industry and answer questions about data broker practices and the difficulty of deleting personal data. Ultimately, we aim to evaluate and identify gaps in existing law and privacy practices.

## Repository Structure
```
.
├── README.md               # Project documentation
├── _config.yml             # Jekyll site configuration
├── 404.html                # Custom 404 page
├── atom.xml                # Atom feed
├── CNAME                   # Custom domain configuration
├── index.md                # Site homepage content
├── LICENSE.md              # Project license
├── _includes/              # Jekyll includes
│   ├── head.html
│   └── sidebar.html
├── _layouts/               # Jekyll layouts
│   ├── default.html
│   ├── page.html
│   └── post.html
├── _plugins/               # Jekyll plugins
│   └── timeout_error_patch.rb
├── cleaned_data/           # Top-level directory for cleaned data (redundant, consider merging with data/cleaned_data)
│   ├── privacy-policies-scraping.csv
│   └── uq-data-brokers.csv
├── data/                   # Data files and datasets
│   ├── README.md           # Data documentation
│   ├── cleaned_data/       # Processed datasets
│   │   ├── uq-data-brokers.csv
│   │   └── privacy_policies/
│   │       ├── privacy_policies_cleaned.csv
│   │       └── privacy_policies_unique_shuffled.csv
│   ├── processed_data/     # Further processed data
│   │   └── README.md
│   └── raw_data/           # Original datasets
│       ├── privacy_policies/
│       │   └── privacy-policy-scraping-final.csv
│       └── survey/
│           ├── survey_results.csv
│           └── Survey-Questions.pdf
├── data_utils/             # Data processing utilities (Python)
│   ├── __init__.py
│   ├── data_cleaner.py     # Data cleaning functions
│   ├── privacy_policy_analyzer.py
│   └── privacy_policy_extractor.py
├── notebooks/              # Jupyter notebooks for analysis and visualization
│   ├── clearinghouse_analysis.ipynb
│   ├── info-extraction.ipynb
│   ├── privacy-policy-analysis.ipynb
│   ├── README.md
│   ├── survey_analysis.ipynb
│   └── imgs/               # Images used in notebooks
│       ├── controls-privacy-policies.png
│       ├── data-collection-practices.png
│       ├── data-sharing-privacy-policies.png
│       ├── permitted-data-use-cases-in-privacy-policies-of-data-brokers.png
│       ├── permitted-entity-data-sharing-in-privacy-policies-of-data-brokers.png
│       ├── transparency-gaps.png
│       ├── use-cases-privacy-policies.png
│       └── user-rights-and-controls-in-privacy-policies-of-data-brokers.png
└── public/                 # Static assets for the Jekyll site
    ├── apple-touch-icon-144-precomposed.png
    ├── favicon.ico
    └── css/
        ├── hyde.css
        ├── poole.css
        └── syntax.css
```

## Website
This project includes a static website built with Jekyll, hosted on GitHub Pages. The content for the site is located in the root directory.

The live website can be viewed at: [https://mjayjoh.github.io/data-broker-analysis/](https://mjayjoh.github.io/data-broker-analysis/)

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