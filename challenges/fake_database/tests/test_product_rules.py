import pytest
from rules import prod_rules
from rules.prod_rules import CONFIG


def test_is_product_name_valid():
    assert prod_rules.is_product_name_valid('egg') == True
    assert prod_rules.is_product_name_valid('egg@') == False
    assert prod_rules.is_product_name_valid('cola 123') == True


def test_is_product_name_long():
    assert prod_rules.is_product_name_long('egg') == True
    assert prod_rules.is_product_name_long('a' * CONFIG['max_name_length']) == True
    assert prod_rules.is_product_name_long('a' * (CONFIG['max_name_length'] + 1)) == False
    assert prod_rules.is_product_name_long('a' * (CONFIG['min_name_length'] - 1)) == False
    assert prod_rules.is_product_name_long('@afdfsdfdf') == True


def test_is_product_description_valid():
    assert prod_rules.is_product_description_valid('Fresh red apple') == True
    assert prod_rules.is_product_description_valid('Fresh apple@') == False
    assert prod_rules.is_product_description_valid('cola 123') == True
    assert prod_rules.is_product_description_valid('') == False
    assert prod_rules.is_product_description_valid('123456') == True


def test_is_product_description_long():
    assert prod_rules.is_product_description_long('Fresh apple') == True
    assert prod_rules.is_product_description_long('a' * CONFIG['max_desc_length']) == True
    assert prod_rules.is_product_description_long('a' * (CONFIG['max_desc_length'] + 1)) == False
    assert prod_rules.is_product_description_long('a' * CONFIG['min_desc_length']) == True
    assert prod_rules.is_product_description_long('a' * (CONFIG['min_desc_length'] - 1)) == False
    assert prod_rules.is_product_description_long('@' * 20) == True

def test_contains_only_digits_floats():
    assert prod_rules.contains_only_digits('12334') == True
    assert prod_rules.contains_only_digits('123.34') == True
    assert prod_rules.contains_only_digits('2342ab3') == False
    assert prod_rules.contains_only_digits('abc') == False
    assert prod_rules.contains_only_digits('123...57') == True
    assert prod_rules.contains_only_digits('') == False

def test_contains_only_digits_integers():
    assert prod_rules.contains_only_digits('12334', is_float=False) == True
    assert prod_rules.contains_only_digits('123.34', is_float=False) == False
    assert prod_rules.contains_only_digits('2342ab3', is_float=False) == False
    assert prod_rules.contains_only_digits('abc', is_float=False) == False
    assert prod_rules.contains_only_digits('123...57', is_float=False) == False
    assert prod_rules.contains_only_digits('', is_float=False) == False


def test_convert_valid_price_to_float():
    assert prod_rules.convert_valid_price_to_float('12334') == 12334.0
    assert prod_rules.convert_valid_price_to_float('123.456') == 123.456
    assert prod_rules.convert_valid_price_to_float('123,456') == 123.456
    assert prod_rules.convert_valid_price_to_float('123..456') == None
    assert prod_rules.convert_valid_price_to_float('123.4.56') == None

def test_is_product_tag_long():
    assert prod_rules.is_product_tag_long('computer') == True
    assert prod_rules.is_product_tag_long('a' * CONFIG['max_tag_length']) == True
    assert prod_rules.is_product_tag_long('a' * (CONFIG['max_tag_length'] + 1)) == False
    assert prod_rules.is_product_tag_long('a' * (CONFIG['min_tag_length'] - 1)) == False
    assert prod_rules.is_product_tag_long('afdfsdfdf') == True

def test_is_product_tag_valid():
    assert prod_rules.is_product_tag_valid('egg') == True
    assert prod_rules.is_product_tag_valid('egg@') == False
    assert prod_rules.is_product_tag_valid('cola 123') == False
    assert prod_rules.is_product_tag_valid('cola abc') == False

        
