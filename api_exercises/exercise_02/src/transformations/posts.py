import pandas as pd

def execute_transformation(raw_data: list) -> pd.DataFrame:

    # converts the list to a dataframe in order to perform transformation
    raw_data = pd.DataFrame(raw_data)

    raw_data = raw_data.rename(
        columns={
            'userId': 'fk_user_id',
            'id': 'pk_post_id',
            'title': 'post_title',
            'body': 'post_content'
        }
    )

    # no data transformations are necessary for this dataframe
    return [
        {
            'posts': raw_data
        }
    ]