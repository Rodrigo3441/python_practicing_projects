# def normalize_categories(categories):
#     result = []

#     for cat in categories:
#         cat = cat.lower()

#         if cat not in result:
#             result.append(cat)

#     return result

def normalize_categories(categories):
    return list(
            {
                cat.lower()
                for cat in categories
            }
    )   

categories = [
    "Action",
    "Drama",
    "action",
    "Comedy",
    "DRAMA",
    "Sci-Fi",
    "comedy",
    "ACTION"
]

result = normalize_categories(categories)

for i in result:
    print(i)