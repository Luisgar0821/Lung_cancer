##-----------------------------------------------------------------------
##libraries
import pandas as pd

##-----------------------------------------------------------------------

csv_file= ("./DATASET/lung_cancer_prediction_dataset.csv")
df = pd.read_csv(csv_file)

import pandas as pd

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Información general del dataset 
print("\nInformación del dataset:")
print(df.info())

# Estadísticas básicas de las variables numéricas
print("\nEstadísticas descriptivas:")
print(df.describe())

# valores duplicados
print("\nCantidad de filas duplicadas:", df.duplicated().sum())

# valores nulos en cada columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# valores únicos de algunas columnas clave
print("\nValores únicos en la columna 'Gender':", df['Gender'].unique())
print("Valores únicos en la columna 'Smoker':", df['Smoker'].unique())
print("Valores únicos en la columna 'Lung_Cancer_Diagnosis':", df['Lung_Cancer_Diagnosis'].unique())
