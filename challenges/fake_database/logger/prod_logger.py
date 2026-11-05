LOG_OUTPUT_FILE = 'data/logs/product.log'

def log_product_registration(product):
    with open(LOG_OUTPUT_FILE, 'a') as log_file:
        log_file.write(f"Product registered: {product}\n")