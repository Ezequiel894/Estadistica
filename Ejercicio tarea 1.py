import pandas as pd
import numpy as np
from scipy import stats

# Valores

data = {
    'Valores': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

# Valores
media = np.mean(df['Valores'])
mediana = np.median(df['Valores'])
desviacion_estandar = np.std(df['Valores'])
varianza = np.var(df['Valores'])
rango = np.ptp(df['Valores'])  # Peak-to-peak (máximo - mínimo)
cuartiles = np.percentile(df['Valores'], [25, 50, 75])
moda = stats.mode(df['Valores'])[0][0]
asimetria = stats.skew(df['Valores'])
curtosis = stats.kurtosis(df['Valores'])

# Resultados

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar}")
print(f"Varianza: {varianza}")
print(f"Rango: {rango}")
print(f"Cuartiles: {cuartiles}")
print(f"Moda: {moda}")
print(f"Asimetría: {asimetria}")
print(f"Curtosis: {curtosis}")
