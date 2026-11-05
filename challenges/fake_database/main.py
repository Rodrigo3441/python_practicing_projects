from ui import helper

menu_cases = [
    'Register product',
    'List all products',
    'Search product',
    'Update product',
    'Delete product',
    'Inventory statistics',
    'Exit'
]

def main():
    print('='*50)
    print('MINICORE INVENTORY↨♥♦☺☻')
    print('='*50)
    print()

    for idx, case in enumerate(menu_cases):
        print(f'{idx+1}. {case}')


    c_option = input().strip()

    match (c_option):
        case '1':
            helper.register_product()

main()
