from api import JsonPlaceholderAPI as api

def run_extraction(base_url: str, data_sources: list) -> list:

    json_api = api.JsonPlaceholderAPI(base_url, data_sources)

    raw_data = []

    raw_data.append(json_api.get_posts())
    raw_data.append(json_api.get_comments())
    raw_data.append(json_api.get_albums())
    raw_data.append(json_api.get_photos())
    raw_data.append(json_api.get_todos())
    raw_data.append(json_api.get_users())

    # posts_data = json_api.get_posts()
    # comments_data = json_api.get_comments()
    # albums_data = json_api.get_albums()
    # photos_data = json_api.get_photos()
    # todos_data = json_api.get_todos()
    # users_data = json_api.get_users()

    return raw_data