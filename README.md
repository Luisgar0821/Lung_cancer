# 🚀 ETL Project - Lung Cancer Prediction 🏥🩺

## 👩‍💻 Developed by:
- 🎓 Juliana Toro
- 🎓 Antonio Cardenas
- 🎓 Luis Angel Garcia

---

## 📌 Overview

📊 In this project, we decided to use a dataset found on Kaggle 📂 containing approximately **221,000 records** and **24 columns**.

🎯 The goal of this project is to perform **data extraction, analysis, and loading** to conduct an **Exploratory Data Analysis (EDA)** and generate **visualizations** 📈 to gain a comprehensive understanding of lung cancer prediction. 🫁

---

## 🛠️ Tools Used

- 🐍 **Python**
- 📒 **Jupyter**
- 🛢️ **XAMPP MySQL**
- 📊 **Power BI**

### 📦 Libraries Used

- 🔗 **mysql.connector**
- 🐼 **pandas**
- 🔢 **numpy**
- 📉 **matplotlib**
- 🎨 **seaborn**

⚡ All libraries are preloaded in **mi_env**.

---

## 📋 Dataset Information

### 📌 Key Variables

- 🆔 **ID**: Unique identifier for each sample.
- 🌍 **Country**: Patient's country of origin.
- 👥 **Population_Size**: Country's population (in millions).
- 👶👩‍🦳 **Age**: Patient's age.
- 🚻 **Gender**: Gender (**Male/Female**).
- 🚬 **Smoker**: Indicates if the person smokes (**Yes/No**).
- ⏳ **Years_of_Smoking**: Years of tobacco consumption.
- 🚭 **Cigarettes_per_Day**: Number of cigarettes smoked per day.
- 🌫️ **Passive_Smoker**: Indicates if the person is exposed to secondhand smoke (**Yes/No**).
- 🧬 **Family_History**: Indicates if there is a family history of lung cancer (**Yes/No**).
- ⚕️ **Lung_Cancer_Diagnosis**: Lung cancer diagnosis (**Yes/No**).
- 🏥 **Cancer_Stage**: Cancer stage (**only 407 records contain data in this column**).
- ⏳ **Survival_Years**: Years of survival after diagnosis.
- 🔬 **Adenocarcinoma_Type**: Type of adenocarcinoma identified.
- 🌎 **Air_Pollution_Exposure**: Level of air pollution exposure (**Low/Medium/High**).
- 🏭 **Occupational_Exposure**: Occupational exposure to carcinogenic substances (**Yes/No**).
- 🏡 **Indoor_Pollution**: Exposure to indoor pollution (**Yes/No**).
- 🏥 **Healthcare_Access**: Level of healthcare access (**Good/Poor**).
- 🔍 **Early_Detection**: Whether cancer was detected early (**Yes/No**).
- 💉 **Treatment_Type**: Type of treatment received (**only 288 records contain data**).
- 🌍 **Developed_or_Developing**: Country classification (**Developed/Developing**).
- ⚰️ **Annual_Lung_Cancer_Deaths**: Annual lung cancer deaths in the country.
- 📊 **Lung_Cancer_Prevalence_Rate**: Lung cancer prevalence rate in the population.
- ⚕️ **Mortality_Rate**: Lung cancer mortality rate.

---

## 🚀 Running the Project

### 📥 Cloning the Repository

First, clone the repository from GitHub using the following command:

```bash
git clone https://github.com/Luisgar0821/Lung_cancer
```

### 🖥️ Opening in Visual Studio Code

Open the cloned repository in **Visual Studio Code**. We recommend selecting the **mi_env kernel** before running the project.

📷 *![image](https://github.com/user-attachments/assets/8762fddc-d4d0-4d2f-8fc3-41d7936e5051)*

### 🔧 MySQL Configuration

💡 **Recommendation:** Install **XAMPP** since its default credentials allow us to configure only the port in the `config.txt` file if necessary.

1️⃣ Start **MySQL** from **XAMPP** to begin working, ensuring it runs on port **3306**.

📷 *![image](https://github.com/user-attachments/assets/be51cf4d-2203-47c0-b056-795395318872)*

2️⃣ If it's not on port **3306**, update the port in `config.txt`.

3️⃣ If using another MySQL tool (e.g., **MySQL Workbench**), start the server and update the credentials in `config.txt` accordingly.

📷 *![image](https://github.com/user-attachments/assets/cca44b1c-47bc-48b9-8a0e-78018a9d56d3)*

### ▶️ Running the Notebook

Finally, simply execute the notebook **cell by cell**. The notebook will handle the **creation of the database and tables** as well as the **ingestion of relevant data**. 🚀📊


