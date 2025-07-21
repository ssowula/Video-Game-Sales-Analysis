Video Game Sales Analysis
This project provides an in-depth analysis of the Video Game Sales dataset from Kaggle. The main goal is to uncover trends and insights related to game sales across different genres, platforms, publishers, and regions.

The full analysis and narrative are presented in the analysis.ipynb Jupyter Notebook.

Key Findings & Visualizations
1. Top 10 Publishers by Global Sales
The analysis shows that the market is dominated by a few major publishers, with Nintendo and Electronic Arts leading the industry.

![Top Publishers](charts/top_10_publishers.png))

2. Total Sales by Genre
Action and Sports are the highest-grossing genres, likely due to their broad appeal and annual releases of popular franchises.

![Sales by Genre](charts/total_sales_by_genre.png))

3. Sales Correlation: Europe vs. North America
There is a strong positive correlation between sales in Europe and North America, which suggests that player preferences in these two key markets are very similar.

![Correlation Plot](charts/cor_and_regression.png))

Technologies Used
Python

pandas

Matplotlib

Seaborn

Jupyter Notebook

Setup and Usage
To run this analysis locally, follow these steps:

Clone the repository:

Bash

git clone https://github.com/ssowula/Video-Game-Sales-Analysis.git
cd Video-Game-Sales-Analysis

Install dependencies:
It is recommended to use a virtual environment.

Bash

pip install -r requirements.txt
Run Jupyter Notebook:

Bash

jupyter notebook analysis.ipynb