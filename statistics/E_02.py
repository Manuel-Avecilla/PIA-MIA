"""

2. Escribe compare_means(nums) que reciba una lista de números positivos y devuelva 
un dict con: 
media aritmética (mean), 
media armónica (harmonic_mean),
media geométrica (geometric_mean),
desviación poblacional (pstdev) y 
coeficiente de variación (cv = pstdev/mean).

"""

import statistics

def compare_means(nums) -> dict:
    
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    if n == 0:
        return {
            "mean": None,
            "harmonic_mean": None,
            "geometric_mean": None,
            "pstdev": None,
            "cv": None
        }
    
    mean = statistics.mean(sorted_nums)
    harmonic_mean = statistics.harmonic_mean(sorted_nums)
    geometric_mean = statistics.geometric_mean(sorted_nums)
    pstdev = statistics.pstdev(sorted_nums)
    cv = pstdev / mean
    
    return {
        "mean": mean,
        "harmonic_mean": harmonic_mean,
        "geometric_mean": geometric_mean,
        "pstdev": pstdev,
        "cv": cv
    }

datos = compare_means([1,2,3,4,5,5,6,7,8,3,34,5,2,1,35,4,3,31,1,34,34,5,1,2,3,5])

for key, value in datos.items():
    print(f"{key}: {value}")

