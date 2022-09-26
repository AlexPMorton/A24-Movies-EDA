# Exploratory Data Analysis for Released A24 Movies

##  Description

I enjoy watching lots of movies and I noticed that some of my favorite movies were being produced or distributed by **A24**. I thought it would be interesting to analyze the movies from **A24** and see if there are any trends or patterns in certain things like budget, revenues, rating, title length, and few others. I also added data on whether the movies had won an oscar or not. The biggest issue for me was not being able to find all the data and whether the movies or columns with the empty values should be removed. The column with the most null values was the budget. I decided to keep the null data it in and make them a part of my analysis. This is an exploratory data analysis (EDA) on all the released movies from [A24](https://a24films.com/films) up to 8/31/2022.

For this project, I used a few different languages/software for following purposes:
- **Excel**: Storing and cleaning all the movie data
- **Python**:
  - **Requests, BeautifulSoup** - Scraping Wikipedia article for Academy Award winners data and exporting CSV file
  - **Pandas** - Analyzing the data
  - **Matplotlib** - Creating visualizations
- **Jupyter Notebooks**: Recording all the information and the process for this entire project 
- **SQL**: Joining the A24 movies and Academy Award winners table together and adding oscar_win column
