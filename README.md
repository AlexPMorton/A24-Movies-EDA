# Exploratory Data Analysis for Released A24 Movies

I enjoy watching lots of movies and I noticed that some of my recent favorites were produced and/or distributed by A24. I thought it would be interesting to analyze the movies from A24 and see if there are any trends or patterns in certain things like budget, revenues, rating, title length, and few others. I also added data on whether the movies had won an oscar or not. The biggest issue for me was not being able to find all the data and whether the movies or columns with the empty values should be removed. The column with the most null values was the budget. I decided to keep the null data in it and make it a part of my analysis. This is an exploratory data analysis (EDA) on all the released movies from [A24](https://a24films.com/films) up to 8/31/2022.

## Programming Languages/Software

In this project, I used a few different tools for the following purposes:

- **Excel**: Storing and cleaning all the movie data
- **Python**:
  - **Requests, BeautifulSoup** - Scraping Wikipedia article for Academy Award winners data and exporting CSV file
  - **Pandas** - Analyzing the data
  - **Matplotlib** - Creating visualizations
- **Jupyter Notebooks**: Documenting all the information and processes for this project 
- **PostgreSQL**: Joining the A24 movies and Academy Award winners table together and adding oscar_win column

## Data Sources

- [A24 Films](https://a24films.com/films) \- List of released movies from A24, release dates, and directors
- [Academy Award winners](https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films) \- List of Academy Award winners
- [Box Office Mojo](https://www.boxofficemojo.com/) \- Revenue, runtime, rating, and some budget data
- [The Numbers](https://www.the-numbers.com/) \- Budget, runtime, rating, and some revenue data when wasn't found on Box Office Mojo
- Wikipedia \- Budget data and for determining genres of the movies
