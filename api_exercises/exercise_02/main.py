# Exercise: Classes, APIs and Pandas
# Practice using a custom Python class to perform HTTP requests to the
# JSONPlaceholder API and convert the returned JSON data into DataFrames.

from api import JsonPlaceholderAPI as api
import pandas as pd

from api import JsonPlaceholderAPI as api
import pandas as pd

def print_separator():
    print("=================================================")

def main():
    url = 'https://jsonplaceholder.typicode.com/posts/'

    json_api = api.JsonPlaceholderAPI(url)
    response = json_api.get_posts()
    response_dict = response.json()

    print_separator()
    print(f'THE RESPONSE TYPE: {type(response)}')
    # print(f'The response content: {response_dict}')

    response_df = pd.DataFrame(response_dict)

    print_separator()
    print('DATAFRAME:')
    print(response_df)

    print_separator()
    print('GET POST BY ID:')
    print(pd.DataFrame([json_api.get_post_by_id(1).json()]))

    print_separator()
    print('GET POSTS BY USER ID:')
    print(pd.DataFrame(json_api.get_posts_by_user(1).json()))

    print_separator()
    print('CREATE POST:')
    print(pd.DataFrame([json_api.create_post('New Post', 'This is a new post.', 1).json()]))


if __name__ == '__main__':
    main()