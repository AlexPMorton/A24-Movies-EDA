import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter,FuncFormatter

# Gets the current working directory
cwd = os.getcwd()

rel_path = "Google Data Analytics Certificate\Case Studies\Case Study 3\A24 Oscars\\a24_released_movies_and_oscars.csv"

# Adding file path to the CSV file with the current working directory
file_path = os.path.join(cwd, rel_path)

# Reading CSV file into a dataframe
A24 = pd.read_csv(file_path)

# Display n rows of the dataframe
print(A24.head(n = 10))

print(A24.info())

pd.options.display.float_format = '{:,.2f}'.format

print(A24.describe())


# Looking at NULL values in budget


# New dataframe for classifying which movies have budget data
A24_budget = A24.copy()

# Adding new column for distinguishing where a mvoie has budget data
A24_budget['has_budget'] = np.select([A24_budget['budget'].isnull(), A24_budget['budget'].notnull()], ['NO','YES'], default='Unknown')
A24_budget_grouped = A24_budget.groupby(['has_budget']).mean()

# New dataframe for all movies with or without budget data
A24_budget_all = A24.copy()

# Adding new column for grouping by all movies with or without budget data
A24_budget_all['has_budget'] = np.select([A24_budget['budget'].any()], ['YES OR NO'], default='Unknown')
A24_budget_all_grouped = A24_budget_all.groupby(['has_budget']).mean()

# Combining the two data frames together
A24_budgets = pd.concat([A24_budget_grouped,A24_budget_all_grouped], sort = False)

# Creating plot for average revenues vs. availability of budget data
budgets_revenues_plot = A24_budgets[['domestic_revenue','international_revenue','worldwide_revenue']].plot(kind='bar', figsize = (10,10/1.5), color = ['orange','tomato','darkviolet'], rot = 1,
xlabel='Does Movie Have Budget Data?', ylabel='Average Revenue (USD)',
title='Average Revenues of Movies Based on Availability of Budget Data')

# Formating the y axis
budgets_revenues_plot.yaxis.set_major_formatter('${x:,.0f}')

plt.show();