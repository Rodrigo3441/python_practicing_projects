# made by rodrigo sg march 9th 2026

import insertion_sort as ins_sort
import select_sort as sel_sort
import bubble_sort as bub_sort
import time

numbers = [17, 3, 29, 8, 14, 1, 25, 11, 30, 6, 19, 4, 27, 13, 2, 21, 9, 24, 7, 16, 28, 5, 22, 10, 18, 26, 12, 20, 15, 23]

runs, comparisons, replacements, arr = bub_sort.bubble_sort(numbers)


print(f'Executions Number: {runs}')
print(f'Comparisons Number: {comparisons}')
print(f'Replacementes: {replacements}')
print(f'Array Organized: {arr}')

