import pandas as pd

def execute_transformation(raw_data: list) -> pd.DataFrame:

    # converts the list to a dataframe in order to perform transformation
    raw_data = pd.DataFrame(raw_data)

    raw_data = raw_data.rename(
        columns={
            'postId': 'fk_post_id',
            'id': 'pk_comment_id',
            'name': 'comment_name',
            'email': 'comment_email',
            'body': 'comment_content'
        }
    )

    # no data transformations are necessary for this dataframe
    return [
        {
            'comments': raw_data
        }
    ]
        
