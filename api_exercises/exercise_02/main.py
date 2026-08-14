# Exercise: Classes, APIs and Pandas
# Practice using a custom Python class to perform HTTP requests to the
# JSONPlaceholder API and convert the returned JSON data into DataFrames.

from api import JsonPlaceholderAPI as api
from src import extract
import pandas as pd

def main():
    base_url = 'https://jsonplaceholder.typicode.com'
    data_sources = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

    raw_data = extract.run_extraction(base_url, data_sources)

    print(pd.DataFrame(raw_data[5]).dtypes)  # Display the data types of the 'users' DataFrame
    


if __name__ == '__main__':
    main()