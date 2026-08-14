def load_data(cleaned_data: dict):
    for table_name, dataframe in cleaned_data.items():
        dataframe.to_csv(f'./api_exercises/exercise_02/data/{table_name}.csv', index=False)