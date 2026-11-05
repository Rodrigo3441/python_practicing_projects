import json

def add_product(product: dict):
    """
    Exports the product to the folder data/products as a json file.
    """

    product_name = product['name']
    product_file_path = f'data/products/{product_name}.json'

    with open(product_file_path, 'w', encoding='utf-8') as file:
        json.dump(product, file, indent=4)