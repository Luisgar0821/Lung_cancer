import pandas as pd

##-----------------------------------------------------------------------

csv_file= ("./DATASET/lung_cancer_prediction_dataset.csv")
df = pd.read_csv(csv_file)

##-----------------------------------------------------------------------
# Mostrar las primeras filas del dataset
print("\nPrimeras filas del dataset:")
print(df.head())

##-----------------------------------------------------------------------
# Información general del dataset 
print("\nInformación del dataset:")
print(df.info())

##-----------------------------------------------------------------------
# Estadísticas básicas de las variables numéricas
print("\nEstadísticas descriptivas:")
print(df.describe())

##-----------------------------------------------------------------------
# valores duplicados
print("\nCantidad de filas duplicadas:", df.duplicated().sum())

# valores nulos en cada columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

##-----------------------------------------------------------------------
# valores únicos 

print("\nValores únicos en la columna 'Gender':", df['Gender'].unique())
print("Valores únicos en la columna 'Smoker':", df['Smoker'].unique())
print("Valores únicos en la columna 'Passive_Smoker':", df['Passive_Smoker'].unique())
print("Valores únicos en la columna 'Family_History':", df['Family_History'].unique())
print("Valores únicos en la columna 'Lung_Cancer_Diagnosis':", df['Lung_Cancer_Diagnosis'].unique())
print("Valores únicos en la columna 'Cancer_Stage':", df['Cancer_Stage'].unique())
print("Valores únicos en la columna 'Adenocarcinoma_Type':", df['Adenocarcinoma_Type'].unique())
print("Valores únicos en la columna 'Air_pollution_exposure':", df['Air_Pollution_Exposure'].unique())
print("Valores únicos en la columna 'Occupational_Exposure':", df['Occupational_Exposure'].unique())
print("Valores únicos en la columna 'Indoor_pollution':", df['Indoor_Pollution'].unique())
print("Valores únicos en la columna 'Healtcare_Access':", df['Healthcare_Access'].unique())
print("Valores únicos en la columna 'Early_Detection':", df['Early_Detection'].unique())
print("Valores únicos en la columna 'Developed_or_Developing':", df['Developed_or_Developing'].unique())

##-----------------------------------------------------------------------
## verificacion de Cigarettes_per_Day

min_cigarettes = df["Cigarettes_per_Day"].min()
max_cigarettes = df["Cigarettes_per_Day"].max()

print(f"\nLos minimos cigarrillos al dia encontrados fueron: ",min_cigarettes)
print(f"Los maximos cigarrillos al dia encontrados fueron: ",max_cigarettes)

smokers = (df["Cigarettes_per_Day"] > 0).sum()
print(f"\nNúmero de personas que fuman son fumadoras: {smokers}")

df_smokers = df[df["Cigarettes_per_Day"]>0]

q1 = df_smokers["Cigarettes_per_Day"].quantile(0.25)
q3 = df_smokers["Cigarettes_per_Day"].quantile(0.75)
iqr=q3-q1

limit_inf = max(1, q1- 1.5 * iqr)
limit_sup = q3 + 1.5 * iqr

atipic_value= df_smokers[(df_smokers["Cigarettes_per_Day"] < limit_inf) | (df_smokers["Cigarettes_per_Day"]>limit_sup)]

print(f"\nQ1: {q1}, Q3: {q3}, IQR: {iqr}")
print(f"Límite inferior ajustado: {limit_inf}")
print(f"Límite superior: {limit_sup}")
print(f"Número de valores atípicos: {atipic_value.shape[0]}")

##-----------------------------------------------------------------------
## verificacion de Age

age_max = df["Age"].max()
age_min = df["Age"].min()
print(f"\nLa edad maxima es: ", age_max)
print(f"La edad minima es: ", age_min)