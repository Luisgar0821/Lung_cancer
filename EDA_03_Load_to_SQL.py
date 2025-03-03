import EDA_02_Data_cleaning_lung_cancer
import mysql.connector
##-----------------------------------------------------------------
##configuracion de mysql

config = {"host":"localhost","port":3306,"user": "root", "password":"","database":"lung_cancer_cleaned"}

##------------------------------------------------------------------
##conexion con mysql

conn = mysql.connector.connect(host=config["host"],port=config["port"], user=config["user"], password=config["password"])
cursor= conn.cursor()

##------------------------------------------------------------------
## creacion de base de datos si no existe

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
conn.database = config["database"]

##------------------------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS lung_cancer (
               ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
               Age INT,
               Country VARCHAR(50),
               Lung_Cancer_Prevalence_Rate FLOAT,
               Smoker VARCHAR(20),
               Years_of_Smoking INT,
               Cigarettes_per_Day INT,
               Passive_Smoker VARCHAR(20),
               Lung_Cancer_Diagnosis VARCHAR(20),
               Healthcare_Access VARCHAR(20),
               Early_Detection VARCHAR(20),
               Survival_Years INT,
               Developed_or_Developing VARCHAR(20),
               Mortality_Rate FLOAT,
               Annual_Lung_Cancer_Deaths INT,
               Air_Pollution_Exposure VARCHAR(20),
               Occupational_Exposure VARCHAR(20),
               Indoor_Pollution VARCHAR(20),
               Family_History VARCHAR(20),
               Treatment_Type VARCHAR(20),
               Cancer_Stage VARCHAR(20)
               );
""")
conn.commit()
print ("La base de datos y tabla se ha creado con exito")