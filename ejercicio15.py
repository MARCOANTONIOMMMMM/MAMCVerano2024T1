import pandas as pd
import matplotlib.pyplot as plt

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

# Colores 
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightcoral', 'lightblue', 'gold', 'violet', 'lightpink', 'lightgrey', 'cyan']

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(df['Clase'], df['Frecuencia Absoluta'], color=colors)
plt.xlabel('Frecuencia Absoluta')
plt.ylabel('Clase')
plt.title('Gráfica de barras')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()