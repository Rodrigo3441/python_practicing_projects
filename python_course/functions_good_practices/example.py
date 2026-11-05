def calculate_discount(price: float, rate: float) -> float:
    '''
    This function returns the calculated discount
    for the enterned price and rate

    Args:
        price (float): Original product price
        rate (float): Discout rate as number (e.g 20 for 20%)

    returns:
        final_price (float): Final price after applying discount.
    '''
    return price - (price * rate/100)


def DiscPrint(p, r):
    
    print('calculating discount')
    p = p - (p * r/100)
    print(p)


# 1 use snake_case for function names
# load_data_from_file

# 2 use clear descriptive function name
# describe it does, avoid abbreviations

# 3 parameter names describe their values
# avoid abbreviations and single letters

# 4 always describe functions using docstring
# help to remember what the function does

# 5 replace print statements with return statements

# 6 dont change parameter values directly

# 7 use data type hints

# 8 explain args and return in docstring
