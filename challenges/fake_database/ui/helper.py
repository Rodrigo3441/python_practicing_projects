from rules import prod_rules
from database import prod_db
from logger import prod_logger

def register_product():
    t_name = None
    t_description = None
    t_price = None
    t_stock_amount = None
    t_tags = set()

    print('='*50)
    print('Enter the product name: ')

    # name entry
    while True:
        t_name = input().strip().lower()

        if prod_rules.is_product_name_valid(t_name):        
            if prod_rules.is_product_name_long(t_name):
                break
            else:
                print(f'Use enough characters for the product name')
        else: 
            print('Use only letters and digits for the product name')

    # description entry
    print('Enter the product description: ')
    while True:
        t_description = input().strip().lower()

        if prod_rules.is_product_description_valid(t_description):
            if prod_rules.is_product_description_long(t_description):
                break
            else:
                print(f'Use enough characteres for the product description')
        else:
            print('Use only letters and digits for the product description')

    # price entry
    print('Enter the product price: ')
    while True:
        t_price = input().strip()

        if prod_rules.contains_only_digits(t_price):
            t_price = prod_rules.convert_valid_price_to_float(t_price)
            if t_price is not None:
                if t_price > 0:
                    break
                else:
                    print('Enter a price higher than zero')
            else:
                print('Enter a valid number')

        else:
            print('Enter only digits for the product price')

    # stock amount entry
    print('Enter the product stock amount: ')
    while True:
        t_stock_amount = input().strip()

        if prod_rules.contains_only_digits(t_stock_amount, is_float=False):
            t_stock_amount = prod_rules.convert_valid_stock_amount_to_int(t_stock_amount)

            if t_stock_amount is not None:
                if t_stock_amount > 0:
                    break
                else:
                    print('Enter an stock amount higher than zero')
            else:
                print('Enter a valid stock amount')
        else:
            print('Enter only digits for the stock amount')

    # tags entry
    c_tag_menu = True
    print('Enter the product tags: ')
    while c_tag_menu:
        t_tag = input().strip().lower()

        if prod_rules.is_product_tag_valid(t_tag):
            if prod_rules.is_product_tag_long(t_tag):
                t_tags.add(t_tag)
                print('Do you want to enter more tags? (1-yes/2-no)')
                c_tag_option = input()
                if c_tag_option == '1':
                    continue
                else:
                    break
            else:
                print('Use enough characters for the product tag')
        else:
            print('Use only letters for the product tag')

    # report
    print('=' * 40)
    print('         PRODUCT REGISTRATION')
    print('=' * 40)
    print(f'Product name:        {t_name}')
    print(f'Description:         {t_description}')
    print(f'Price:               R$ {t_price:.2f}')
    print(f'Stock amount:        {t_stock_amount}')
    print(f'Tags:                {", ".join(t_tags) if t_tags else "None"}')
    print('=' * 40)

    new_product = {
        'name': t_name,
        'description': t_description,
        'price': t_price,
        'stock_amount': t_stock_amount,
        'tags': list(t_tags)
    }

    prod_db.add_product(new_product)
    prod_logger.log_product_registration(new_product)
    print('Product registered successfully.')





    

    
        

