# Exercise: Classes, APIs and Pandas
# Practice using a custom Python class to perform HTTP requests to the
# JSONPlaceholder API and convert the returned JSON data into DataFrames.

from api import JsonPlaceholderAPI as api
from src import extract
from src import transform
from src import load

def main():
    base_url = 'https://jsonplaceholder.typicode.com'
    data_sources = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

    raw_data = extract.run_extraction(base_url, data_sources)
    cleaned_data: list = transform.run_transformations(raw_data)
    load.load_data(cleaned_data)

if __name__ == '__main__':
    main()