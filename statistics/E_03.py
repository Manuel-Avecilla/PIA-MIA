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

def normal_tasks(data, x, p) -> dict:
    
    if len(data) == 0:
        return {
            "mean": None,
            "stdev": None,
            "cdf": None,
            "inv_cdf": None,
            "z_score": None
        }
    
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    
    NorD = statistics.NormalDist(mu=mean, sigma=stdev)
    
    cdf = NorD.cdf(float(x))
    inv_cdf = NorD.inv_cdf(float(x))
    
    z_score = (x - mean)/stdev
    
    return {
        "mean": mean,
        "stdev": stdev,
        "cdf": cdf,
        "inv_cdf": inv_cdf,
        "z_score": z_score
    }

datos = normal_tasks([1,2,3,4,5,5,6,7,8,3,34,5,2,1,35,4,3,31,1,34,34,5,1,2,3,5], 0.4, 3)

for key, value in datos.items():
    print(f"{key}: {value}")

