import re

CONFIG = {
    'min_name_length': 3,
    'max_name_length': 40,
    'min_desc_length': 10,
    'max_desc_length': 100,
    'min_tag_length': 3,
    'max_tag_length': 20
}

def is_product_name_valid(name: str) -> bool:
    return bool(re.match(r'^[a-zA-ZÀ-ÿ0-9 ]+$', name))

def is_product_name_long(name: str) -> bool:
    return CONFIG['min_name_length'] <= len(name) <= CONFIG['max_name_length']

def is_product_description_valid(description: str) -> bool:
    return bool(re.match(r'^[a-zA-ZÀ-ÿ0-9 ]+$', description))

def is_product_description_long(description: str) -> bool:
    return CONFIG['min_desc_length'] <= len(description) <= CONFIG['max_desc_length']

def contains_only_digits(price: str, is_float=True) -> bool:
    '''
    This function returns either if a string matches an int/float regex containing only numbers or dots and quomas

    Params:
        price: an string that represents a int / float number
        is_float: a boolean value that indicates if a string represents a float number or a integer number(default=True)

    '''
    regex_exp = '^[0-9.,]+' if is_float else '^[0-9]+'

    return bool(re.fullmatch(regex_exp, price))

def convert_valid_price_to_float(price: str) -> float | None:
    '''
    This function will receive a string number value and convert it into float

    Returns
        Returns a float number from a string, returns None if the string is not valid
    '''
    if price.count('.') > 1:
        return None
    
    normalized_price = price.replace(',','.')
    return float(normalized_price)

def convert_valid_stock_amount_to_int(stock_amount: str) -> int | None:
    return int(stock_amount)

def is_product_tag_long(tag: str) -> bool:
    return CONFIG['min_tag_length'] <= len(tag) <= CONFIG['max_tag_length']

def is_product_tag_valid(tag: str) -> bool:
    return bool(re.match(r'^[a-zA-ZÀ-ÿ]+$', tag))