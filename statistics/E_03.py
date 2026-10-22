"""

3. Dado un conjunto data de observaciones, ajusta una normal usando la media y desviación poblacional del conjunto.
Crea una función normal_tasks(data, x, p) que:

Cree un NormalDist ajustado a data.
Calcule la probabilidad P(X <= x) (CDF).
Calcule el percentil (inversa) inv_cdf(p): el valor y tal que P(X <= y) = p.
Devuelva además el z-score de x usando (x - mean)/stdev.

Usa statistics.NormalDist.

"""

import statistics

def normal_tasks(data, x, p):
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n == 0:
        return None
    
    mean = statistics.mean(sorted_data)
    stdev = statistics.stdev(sorted_data)
    
    NorD = statistics.NormalDist(mu=mean, sigma=stdev)
    
    
    
    
    
    pass

