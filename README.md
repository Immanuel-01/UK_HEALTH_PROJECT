# 🩺 UK Mortality Risk Prediction  
**Author:** Emmanuel Okunfolami  

A machine learning + BI project predicting mortality rates across UK patient cohorts using demographic, treatment, cost, and healthcare access data.

This project combines a predictive ML pipeline, interactive visualizations (Power BI), and a deployed Streamlit app to support insights into health inequality, treatment effectiveness, and mortality risk prediction.

---

## 📘 Project Overview

This project addresses a key question:  
**Can we predict patient mortality risk based on treatment types, healthcare access, and demographic factors across disease categories in the UK?**

---

## 🎯 Key Objectives

- Predict mortality risk using regression-based ML models  
- Highlight treatment disparities across gender, age group, and disease type  
- Visualize relationships between cost, healthcare access, and DALYs  
- Provide an interactive tool for simulation and decision-making  

---

## 📁 Project Structure

UK_HEALTH_PROJECT/ │ ├── Data/ │ ├── Raw/ # Raw source data │ └── Processed/ # Cleaned, encoded dataset for modeling │ ├── uk_mortality_app/ │ ├── models/ # Trained model & scaler (pkl) │ ├── app.py # Streamlit app │ └── requirements.txt # Deployment dependencies │ ├── step_0_clean_data.py # Data cleaning ├── step_1_prepare_features.py # Encoding & feature prep ├── step_2_train_model.py # Model training & evaluation ├── step_3_generate_predictions.py # (Optional) Batch prediction │ └── PowerBI_Report.pdf # Dashboard visuals (featured in README)


---

## 🚀 Streamlit App

Use the live app to simulate mortality risk based on:
- Gender  
- Age Group  
- Disease Category  
- Treatment Type  
- Healthcare Access (%)  
- Treatment Cost (USD)  

👉 **Live Demo**: [UK Mortality Predictor](https://huggingface.co/spaces/EOEOkunfolami/UK_Mortality_Predictor)

---

## 📊 Power BI Dashboard

- **Page 1**: Overview — predicted vs actual mortality rate by treatment type, plus demographic filters
  ![Screenshot (584)](https://github.com/user-attachments/assets/df411f83-f5d4-47f2-917a-277d8d5162b3)

- **Page 2**: Deep Dive — DALYs, cost implications, and yearly mortality trend lines
  ![Screenshot (583)](https://github.com/user-attachments/assets/26e472ff-9b12-4349-b478-375f75a113fa)


*(See screenshots included in this repo)*

---

## 🧠 Model Info

- **Type**: Linear Regression  
- **Metrics**: MSE, R² Score  
- **Preprocessing**: One-hot encoding + StandardScaler  
- **Target Variable**: `Mortality Rate (%)`

---

## 🛠 Installation (Local)

```bash
git clone https://github.com/Immanuel-01/UK_HEALTH_PROJECT.git
cd UK_HEALTH_PROJECT/uk_mortality_app
pip install -r requirements.txt
streamlit run app.py

🙏 Acknowledgements
UK open healthcare datasets

Streamlit + Hugging Face Spaces

Python, Pandas, Scikit-learn, Power BI

DAX for Power BI modeling and calculations

⚠️ Disclaimer
This project was created for educational and portfolio purposes only.
It is not intended for clinical or diagnostic use.



---
