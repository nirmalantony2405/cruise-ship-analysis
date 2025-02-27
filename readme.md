# Cruise Ship Performance Analysis 

## Overview 

This repository contains a detailed performance analysis of two cruise ships, Vessel 1 and Vessel 2. The project examines key trends in efficiency, propulsion, and power generation, based on a provided dataset. The analysis complies with international regulatory requirements for shipping and includes industry-relevant Key Performance Indicators (KPIs).

The project is implemented using Python, with Jupyter notebooks guiding the analysis and Python modules providing reusable functionality for data processing, feature engineering, and visualization.

## Setup and Installation

To run the code in this repository, ensure you have the following prerequisites:

### Hardware: 
A standard modern laptop with a 4-core CPU and 16 GB RAM.
### Software:
    ◦ Python 3.8 or higher
    ◦ Jupyter Notebook or JupyterLab
    ◦ Git (for cloning the repository)

### Dependencies
The project relies on the following Python packages:

◦ pandas>=1.5.0

◦ numpy>=1.23.0

◦ matplotlib>=3.5.0

◦ seaborn>=0.11.0

Install these dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

## Running the Code
Clone the repository:
```bash
git clone https://github.com/your-username/cruise-ship-analysis.git
cd cruise-ship-analysis
```

### Navigate to the notebooks/ directory and run the Jupyter notebooks in this order:
◦ data_exploration.ipynb: Initial exploration and quality assessment of  the dataset.

◦ data_cleaning.ipynb: Data preprocessing and cleaning.

◦ vessel_comparison.ipynb: Comparison of Vessel 1 and Vessel 2 performance metrics.

◦ efficiency_analysis.ipynb: Analysis of efficiency metrics like fuel consumption and power usage.

◦ kpi_dashboard.ipynb: Visualization of KPIs in a dashboard format.
### View results: 
After running the notebooks, check the reports/ directory for generated figures and the final report.
Each notebook includes detailed explanations and can be run independently, provided the data files are in the data/raw/ directory.

## Repository Structure
The repository is organized as follows:

```
cruise-ship-analysis/
├── README.md                           # Project overview and instructions
├── data/                               # Data directory
│   ├── data.csv                        # Raw cruise ship data
│   ├── processed/                      # Cleaned and transformed data
│   └── schema.pdf                      # Data schema description
├── notebooks/                          # Jupyter notebooks
│   ├── 01_data_exploration.ipynb       # Initial data examination
│   ├── 02_data_cleaning.ipynb          # Data preprocessing and cleaning
│   ├── 03_vessel_comparison.ipynb      # Vessel performance comparison
│   ├── 04_efficiency_analysis.ipynb    # Efficiency metrics analysis
│   └── 05_kpi_dashboard.ipynb          # KPI visualization
├── src/                                # Source code modules
│   ├── __init__.py
│   ├── data/                           # Data processing utilities
│   │   ├── __init__.py
│   │   ├── loader.py                   # Data loading functions
│   │   └── cleaner.py                  # Data cleaning functions
│   ├── features/                       # Feature engineering
│   │   ├── __init__.py
│   │   └── engineering.py              # Feature creation functions
│   ├── analysis/                       # Analysis modules
│   │   ├── __init__.py
│   │   ├── efficiency.py               # Efficiency calculations
│   └── visualization/                  # Visualization utilities
│       ├── __init__.py
│       └── plotting.py                 # Plotting functions
├── reports/                            # Generated outputs
│   ├── figures/                        # Visualization outputs
│   └── final_report.md                 # Final analysis summary
├── requirements.txt                    # Project dependencies
└── setup.py                            # Package installation script
```
## Key Components

◦ data/data.csv: The original dataset for the analysis.

◦ data/processed/: Cleaned and transformed data generated by the notebooks.

◦ notebooks/: Step-by-step analysis in Jupyter notebooks.

◦ src/: Modular Python code for data handling, analysis, and visualization.

◦ reports/: Outputs including figures and a final report.

## How to Navigate the Repository
### 1. Begin with the notebooks: 
Run them in the numbered order (01 to 05) to follow the analysis workflow:

◦ 01_data_exploration.ipynb: Understand the dataset structure and quality.

◦ 02_data_cleaning.ipynb: Prepare the data for analysis.

◦ 03_vessel_comparison.ipynb: Compare performance between the two vessels.

◦ 04_efficiency_analysis.ipynb: Dive into efficiency metrics.

◦ 05_kpi_dashboard.ipynb: Visualize results and KPIs.

### 2. Explore the source code: 
The src/ directory contains reusable modules imported by the notebooks, including:

◦ Data loading and cleaning (src/data/).

◦ Feature engineering (src/features/).

◦ Analysis functions (src/analysis/).

◦ Plotting utilities (src/visualization/).

### 3. Review outputs:
Check reports/figures/ for visualizations and reports/final_report.md for the analysis summary.

## Programming Languages and Tools 
◦ Primary Language: Python (SQL is supported but not used directly as the data is in CSV format).
◦ Support Files: Configuration files (e.g., JSON, YAML) may be present but are not central to the analysis.

## Additional Notes
◦The project is designed to be reproducible on a standard laptop.
◦All code adheres to the requirement of using only Python and avoids proprietary tools.

## Contact and Issues
For questions or issues, please file a report on the GitHub Issues page of this repository.
