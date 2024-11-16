# Homework 3 - Algorithmic Methods of Data Mining

## Michelin Restaurants in Italy

This repository contains the solution for **Homework 3** of the course *Algorithmic Methods of Data Mining*.

The main goal of this homework is to explore and analyze Michelin restaurant data in Italy. The project includes multiple tasks such as data cleaning, feature extraction, text processing, and visualization.

### Repository Contents

- **`adm_hw3.ipynb`**: A Jupyter Notebook containing Python solutions for Homework 3. It includes code, explanations, and outputs for each question of the assignment.
  
- **`file/`**: A folder containing all output files generated from the homework tasks.
    - **[all_restaurants_data.csv](file/all_restaurants_data.csv)**: Dataset containing all information about Michelin restaurants in Italy, collected from the Michelin website. This file is the output for **Question 1.3**.
    - **[vocabulary.csv](file/vocabulary.csv)**: A CSV file that maps each word in the `description` column of `all_restaurants_data.csv` to a unique integer (`term_id`). This file is the result of **Question 2.1.1**.
    - **[inverted_index.pkl](file/inverted_index.pkl)**: A pickle file containing a dictionary mapping each `term_id` to a list of document IDs where that term appears. This file is the output for **Question 2.1.1**.
    - **[coordinates.csv](file/coordinates.csv)**: A CSV file containing all unique city coordinates in the dataset. This file is the output for **Question 4**.
    - **[top_k_restaurants_map.html](file/top_k_restaurants_map.html)**: An HTML file displaying the top-k Michelin restaurants based on a custom scoring system, visualized on a map. This is the result for **Question 4**.


   
