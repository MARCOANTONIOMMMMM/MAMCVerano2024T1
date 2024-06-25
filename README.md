# MAMCVerano2024T1
import pandas as pd

def calcular_frecuencia_relativa(frecuencia_absoluta):
    return frecuencia_absoluta / frecuencia_absoluta.sum()

def calcular_frecuencia_acumulada(frecuencia_absoluta):
    return frecuencia_absoluta.cumsum()

# Crear los datos
data = {
    'Clase': ['RAMIREZ', 'RODRIGUEZ', 'HERNANDEZ', 'GONZALEZ', 'GARCIA', 'MARTINEZ', 'LOPEZ', 'GUTIERREZ', 'PEREZ', 'SANCHEZ', 'FLORES'],
    'Frecuencia Absoluta': [6, 9, 15, 12, 14, 12, 10, 4, 6, 8, 4]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Calcular Frecuencia Relativa
df['Frecuencia Relativa'] = calcular_frecuencia_relativa(df['Frecuencia Absoluta'])

# Calcular Frecuencia Acumulada
df['Frecuencia Acumulada'] = calcular_frecuencia_acumulada(df['Frecuencia Absoluta'])

# Imprimir el DataFrame
print(df.to_string(index=False))