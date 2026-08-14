import pandas as pd

def execute_transformation(raw_data: list) -> pd.DataFrame:

    # converts the list to a dataframe in order to perform transformation
    raw_data = pd.DataFrame(raw_data)

    raw_data = raw_data.rename(
        columns={
            'userId': 'fk_user_id',
            'id': 'pk_todo_id',
            'title': 'todo_title',
            'completed': 'todo_completed'
        }
    )

    # no data transformations are necessary for this dataframe
    return [
        {
            'todos': raw_data
        }
    ]