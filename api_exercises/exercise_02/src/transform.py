from src.transformations import posts
from src.transformations import comments
from src.transformations import albums
from src.transformations import photos
from src.transformations import todos
from src.transformations import users

def map_transformations(table_name: str, data: list) -> list:

    print(f'Transforming the table \'{table_name}\'')
    match(table_name):
        case 'posts':
            return posts.execute_transformation(data)

        case 'comments':
            return comments.execute_transformation(data)

        case 'albums':
            return albums.execute_transformation(data)

        case 'photos':
            return photos.execute_transformation(data)

        case 'todos':
            return todos.execute_transformation(data)

        case 'users':
            return users.execute_transformation(data)



def run_transformations(raw_data: dict) -> dict:

    cleaned_data = {}

    for table_name, data in raw_data.items():
        list_of_dictionaries = map_transformations(table_name, data)

        for i in list_of_dictionaries:
            cleaned_data.update(i)

    return cleaned_data