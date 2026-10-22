"""

1. Crea five_number_summary(nums) que devuelva (min, Q1, median, Q3, max) usando statistics.
Usa statistics.quantiles para los cuartiles y statistics.median para la mediana.

"""

import statistics


def five_number_summary(nums):

    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    if n == 0:
        return (None, None, None, None, None)
    
    min_val = sorted_nums[0]
    max_val = sorted_nums[-1]
    
    q1 = statistics.quantiles(sorted_nums, n=4)[0]
    
    med = statistics.median(sorted_nums)
    
    q3 = statistics.quantiles(sorted_nums, n=4)[2]
    
    return (min_val, q1, med, q3, max_val)

datos = five_number_summary([1,2,3,4,5,5,6,7,8,3,34,5,2,1,35,4,3,31,1,34,34,5,1,2,3,5])

for i, x in enumerate(datos):
    match i:
        case 0: print("Min: ",x)
        case 1: print("Q1: ",x)
        case 2: print("Median: ",x)
        case 3: print("Q3: ",x)
        case 4: print("Max: ",x)