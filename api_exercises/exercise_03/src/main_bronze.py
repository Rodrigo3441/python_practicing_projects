from database import connection
from api_exercises.exercise_03.src.bronze import extract
from api_exercises.exercise_03.src.bronze import transform
from api_exercises.exercise_03.src.bronze import load

def run():

    engine = connection.get_connection()
    pages = extract.return_total_pages()

    for page in range(1, pages+1):
        raw_data = extract.run(page)
        cleaned_data = transform.run(raw_data)
        print(page)
        load.execute(engine, cleaned_data, 'bronze')