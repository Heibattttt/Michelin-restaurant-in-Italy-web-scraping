# Homework 3 - Algorithmic Methods of Data Mining

## Michelin Restaurants in Italy
![Michelin Restaurant](https://www.chase.com/content/dam/unified-assets/photography/articles/credit-card/basics/seo_michelin-restaurants-that-deliver_101222.jpg)

This repository contains the solution for **Homework 3** of the course *Algorithmic Methods of Data Mining*.

---
The main goal of this homework is to explore and analyze Michelin restaurant data in Italy. The project includes multiple tasks such as data cleaning, feature extraction, text processing and visualization.
To get all the data that we needed, we did a web scraping process of the [*Michelin restaurants site*](https://guide.michelin.com/en/it/restaurants) and we extracted the html of each restaurant on the page and saved it in a folder called [*HTML Michelin Restaurants*](https://www.dropbox.com/scl/fo/0j7jc0ltldfykhayu7yv5/AMGq46jObUCNfQYPiC58QhA?rlkey=3a94pnup3e443yhjwmu5s88wu&st=xog2xz1h&dl=0).

### Repository Contents:
- [**`Project/`**](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/tree/main/Project): A folder containing a notebook file with the progress and comments of the tasks performed and a fil.py with the code of an advanced search engine algorithm. Specifically it includes:
  - [**Michelin-restaurant-in-Italy-web-scraping.ipynb**](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/Project/Scraping%20Michelin%20restaurants.ipynb): A Jupyter Notebook containing Python code, explanations, outputs for each question of the homework and a pseudocode of an algorithm for moving a robot in a warehouse for packages collection. 
    - **Warning:** To view all output from the file please download the file and read it in a supported development environment;
  - [**search_engine_filters.py**](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/Project/search_engine_filters.py): This file was used in `Michelin-restaurant-in-Italy-web` for Bonus part and is an interactive restaurant search engine built with Python and ipywidgets, which offers advanced filtering capabilities. It features an intuitive interface with dynamic drop-down menus and checkboxes.
    - **Warning**: To view the interactive interface, make sure to run the code cell in a environment with `ipywidgets` enabled. *Here is an example of how it works:*
  ![Search Engine](https://github.com/Heibattttt/Michelin-restaurant-in-Italy-web-scraping/blob/main/Images/Advance%20Search%20Engine.png)
---
### Dropbox files used for the project:
- [**`files/`**](https://www.dropbox.com/scl/fo/7ioya39gi8q7yxonv2ey6/AMiAO5f1FqTKBU3MIHP47AU?rlkey=4jp7ujqfyd2y2lz8zuv714771&st=lvvwdwhb&dl=0): A **Dropbox** folder containing all output files generated from the homework tasks. In detail:
  - **[all_restaurants_data.csv](https://www.dropbox.com/scl/fi/b5kopvu3mtrrer51ch43w/all_restaurants_data.csv?rlkey=30u7kxhngucs98q00kijstkkl&st=j0m57lix&dl=0)**: Dataset containing all information about Michelin restaurants in Italy, collected from the Michelin website. This file is the output for **Question 1.3**;
  - **[vocabulary.csv](https://www.dropbox.com/scl/fi/5fdxqt7v5ehaxdaknz8as/vocabulary.csv?rlkey=5mplouit7gngbxu51zezbow00&st=8a6eh3yc&dl=0)**: A CSV file that maps each word in the `description` column of `all_restaurants_data.csv` to a unique integer (`term_id`). This file is the result of **Question 2.1.1**;
  - **[inverted_index.pkl](https://www.dropbox.com/scl/fi/xjs9ejx1xi51a4z72xqz4/inverted_index.pkl?rlkey=pgt50rrwhpq44oe8c61zoonok&st=3yi3gz9c&dl=0)**: A pickle file containing a dictionary mapping each `term_id` to a list of document IDs where that term appears. This file is the output for **Question 2.1.1**;
  - **[coordinates.csv](https://www.dropbox.com/scl/fi/z6igcagtvf3more0geoje/coordinates.csv?rlkey=k6uc86iyrdagcu18xlvyurrqq&st=mtizfjvq&dl=0)**: A CSV file containing all unique city coordinates in the dataset. This file is the output for **Question 4**;
  - **[top_k_restaurants_map.html](https://www.dropbox.com/scl/fi/k16i212xf1obr1sknee3q/top_k_restaurants_map.html?rlkey=pp8057im2puqiv1bbsuv01ivn&st=gg1vx3cx&dl=0)**: An HTML file displaying the top-k Michelin restaurants based on a custom scoring system, visualized on a map. This is the result for **Question 4**. To     view the map you need to download the html file or view the Notebook file on a development environment such as Visual Studio, Jupyter or Pycharm
  



   
