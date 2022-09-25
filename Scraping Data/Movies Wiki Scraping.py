from bs4 import BeautifulSoup
import requests
import pandas as pd

# Function to scrape table data from the Academy Award winners Wikipedia article
def Wiki_Table_Scrape(Academy_Award_winners_wiki_url,html_table_name,Excel_file_name):

    table_class = "wikitable sortable" # name of class for the table in the html file

    response = requests.get(Academy_Award_winners_wiki_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Finds all html attributes with the specific class name
    Table = soup.find_all(html_table_name, attrs={'class': table_class})

    # Converts parsed html file to list
    Wiki_table_list = pd.read_html(str(Table))

    # Converts list  to dataframe
    Wiki_table_df = Wiki_table_list[0]

    # Exports data table to an Excel file
    Wiki_table_df.to_excel(Excel_file_name)

Wiki_Table_Scrape("https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films", 'table', "Academy_Award_Winning_Movies.xlsx")