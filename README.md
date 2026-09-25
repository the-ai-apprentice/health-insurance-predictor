# 🛡️ Health Insurance Premium Predictor

This data-driven machine learning application accurately estimates healthcare insurance premium costs based on applicant demographics, medical history, and lifestyle factors. Developed by AtliQ AI for S.H.E.I.L.D. Insurance, the project leverages advanced regression techniques and model segmentation to provide reliable pricing insights through an interactive web interface.

## 📊 Business Context

S.H.E.I.L.D. Insurance requires a robust predictive model to minimize the financial risks associated with underpricing and overpricing premiums. The successful deployment of this tool targets several key performance indicators:

* Reduce customer attrition by at least 10%.
* Lower the claims ratio by at least 5%.
* Increase overall revenue by 15% within the first six months of deployment.

## ✨ Key Features

* **Model Segmentation:** Implements two specialized machine learning models to maximize prediction accuracy across distinct age demographics (under 25 and over 25).
* **Dynamic Health Risk Scoring:** Translates complex textual medical histories into normalized numerical health risk scores to streamline predictions.
* **Interactive Web Application:** Features a fully functional Streamlit dashboard that allows underwriters to input client variables and instantly view the estimated annual premium.
* **High Accuracy Standards:** Achieves an R² score of >98% utilizing a Linear Regression model for younger applicants (prioritizing explainability) and a highly optimized XGBoost Regressor for adult applicants.

## 📂 Project Structure
