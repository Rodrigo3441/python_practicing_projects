from api import JsonPlaceholderAPI as api

def run_extraction(base_url: str, data_sources: list) -> list:

    json_api = api.JsonPlaceholderAPI(base_url, data_sources)

    return {
        'posts': json_api.get_posts(),
        'comments': json_api.get_comments(),
        'albums': json_api.get_albums(),
        'photos': json_api.get_photos(),
        'todos': json_api.get_todos(),
        'users': json_api.get_users()
    }