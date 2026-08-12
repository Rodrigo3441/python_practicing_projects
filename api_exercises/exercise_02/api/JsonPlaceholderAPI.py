# Exercise: Classes and REST APIs
# Implements a simple API client class for interacting with JSONPlaceholder,
# using class methods to organize GET and POST HTTP operations.

import requests

class JsonPlaceholderAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_posts(self) -> requests.Response:
        return requests.get(self.base_url, timeout=5)

    def get_post_by_id(self, id: int) -> requests.Response:
        return requests.get(f'{self.base_url}/{id}', timeout=5)

    def get_posts_by_user(self, user_id: int) -> requests.Response:
        return requests.get(f'{self.base_url}/?userId={user_id}', timeout=5)

    def create_post(self, title: str, body: str, user_id: int) -> requests.Response:
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return requests.post(self.base_url, json=data, timeout=5)
