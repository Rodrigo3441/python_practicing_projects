import pandas as pd

def execute_transformation(raw_data: list) -> dict:

    # solves the nested jsons for the users data source
    raw_data = pd.json_normalize(raw_data)

    # create the user source dataframe
    user_data = raw_data[
                          [
                            'id',
                            'name',
                            'username',
                            'email',
                            'phone',
                            'website'
                          ]
                        ].copy()

    user_data = user_data.rename(
        columns={
            'id': 'pk_user_id',
            'name': 'user_name',
            'username': 'user_username',
            'email': 'user_email',
            'phone': 'user_phone',
            'website': 'user_website'
        }
    )
    
    # create the user address dataframe with the user id for data aggregations
    user_address_data = raw_data[
                                    [
                                        'id',
                                        'address.street', 
                                        'address.suite', 
                                        'address.city', 
                                        'address.zipcode', 
                                        'address.geo.lat',
                                        'address.geo.lng',
                                    ]
                                ].copy()

    user_address_data = user_address_data.rename(
        columns={
            'id': 'fk_user_id',
            'address.street': 'address_street',
            'address.suite': 'address_suite',
            'address.city': 'address_city',
            'address.zipcode': 'address_zipcode',
            'address.geo.lat': 'address_geo_lat',
            'address.geo.lng': 'address_geo_lng'
        }
    )


    # create the user company dataframe with the user id for data aggregations
    user_company_data = raw_data[
                                    [       
                                        'id',
                                        'company.name',
                                        'company.catchPhrase',
                                        'company.bs'
                                    ]
                                ].copy()

    user_company_data = user_company_data.rename(
        columns={
            'id': 'fk_user_id',
            'company.name': 'company_name',
            'company.catchPhrase': 'company_catch_phrase',
            'company.bs': 'company_bs'
        }
    )

    return [
        { 
            'users': user_data
        },
        {
            'address': user_address_data
        },
        {
            'company': user_company_data
        }
    ]
           