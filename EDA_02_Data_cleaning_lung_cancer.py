import pandas as pd

##-----------------------------------------------------------------------

df= pd.read_csv("./DATASET/lung_cancer_prediction_dataset.csv")

##-----------------------------------------------------------------------
## seleccion

df_selected = df[["ID","Age","Country","Lung_Cancer_Prevalence_Rate","Smoker","Years_of_Smoking","Cigarettes_per_Day","Passive_Smoker","Lung_Cancer_Diagnosis","Healthcare_Access","Early_Detection","Survival_Years","Developed_or_Developing","Mortality_Rate","Annual_Lung_Cancer_Deaths","Air_Pollution_Exposure","Occupational_Exposure","Indoor_Pollution","Family_History","Treatment_Type","Cancer_Stage"]]

df_selected.loc[:, "Cancer_Stage"] = df_selected["Cancer_Stage"].fillna("None")
df_selected.loc[:, "Treatment_Type"] = df_selected["Treatment_Type"].fillna("None")

# valores nulos en cada columna

print("\nValores nulos por columna:")
print(df_selected.isnull().sum())

##-----------------------------------------------------------------------
##ajuste








