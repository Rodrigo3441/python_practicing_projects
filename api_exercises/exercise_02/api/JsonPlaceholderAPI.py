# Exercise: Classes and REST APIs
# Implements a simple API client class for interacting with JSONPlaceholder,
# using class methods to organize GET and POST HTTP operations.

import requests

class JsonPlaceholderAPI:
    def __init__(self, base_url: str, data_sources: list):
        self.base_url = base_url
        self.data_sources = data_sources

    def get_posts(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[0]}', timeout=5).json()
         
    def get_comments(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[1]}', timeout=5).json()

    def get_albums(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[2]}', timeout=5).json()

    def get_photos(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[3]}', timeout=5).json()

    def get_todos(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[4]}', timeout=5).json()

    def get_users(self) -> requests.Response:
        return requests.get(f'{self.base_url}/{self.data_sources[5]}', timeout=5).json()