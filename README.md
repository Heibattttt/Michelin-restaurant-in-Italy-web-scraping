# Homework 3 - Algorithmic Methods of Data Mining

## Michelin Restaurants in Italy
![Michelin Restaurant](https://www.chase.com/content/dam/unified-assets/photography/articles/credit-card/basics/seo_michelin-restaurants-that-deliver_101222.jpg)
This repository contains the solution for **Homework 3** of the course *Algorithmic Methods of Data Mining*.

The main goal of this homework is to explore and analyze Michelin restaurant data in Italy. The project includes multiple tasks such as data cleaning, feature extraction, text processing, and visualization.

### Repository Contents
- [**`Project/`**](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/tree/main/Project): A folder containing a notebook file with the progress and comments of the tasks performed and a .py file with the code of an advanced search algorithm. In detail:
  - **[`Michelin-restaurant-in-Italy-web-scraping`](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/Project/Scraping%20Michelin%20restaurants.ipynb)**: A Jupyter Notebook containing Python solutions for Homework 3. It includes code, explanations, and outputs for each question of the assignment. **Warning:** To view all output from the file please download the file and read it in a supported development environment;
  - **[search_engine_filters.py](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/Project/search_engine_filters.py): This file was used in `Michelin-restaurant-in-Italy-web` and is an interactive restaurant search engine built with Python and ipywidgets, which offers advanced filtering capabilities. It features an intuitive interface with dynamic drop-down menus and checkboxes.
  
- [**`files/`**](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/tree/main/files): A folder containing all output files generated from the homework tasks. In detail:
  - **[all_restaurants_data.csv](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/files/all_restaurants_data.csv)**: Dataset containing all information about Michelin restaurants in Italy, collected from the Michelin website. This file is the output for **Question 1.3**;
  - **[vocabulary.csv](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/files/vocabulary.csv)**: A CSV file that maps each word in the `description` column of `all_restaurants_data.csv` to a unique integer (`term_id`). This file is the result of **Question 2.1.1**;
  - **[inverted_index.pkl](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/files/inverted_index.pkl)**: A pickle file containing a dictionary mapping each `term_id` to a list of document IDs where that term appears. This file is the output for **Question 2.1.1**;
  - **[coordinates.csv](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/files/coordinates.csv)**: A CSV file containing all unique city coordinates in the dataset. This file is the output for **Question 4**;
  - **[top_k_restaurants_map.html](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/raw/main/files/top_k_restaurants_map.html)**: An HTML file displaying the top-k Michelin restaurants based on a custom scoring system, visualized on a map. This is the result for **Question 4**. To     view the map you need to download the html file or view the Notebook file on a development environment such as Visual Studio, Jupyter or Pycharm



   
