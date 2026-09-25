# 🛡️ Health Insurance Premium Predictor

This data-driven machine learning application accurately estimates healthcare insurance premium costs based on applicant demographics, medical history, and lifestyle factors. Developed for S.H.E.I.L.D. Insurance, the project leverages advanced regression techniques and model segmentation to provide reliable pricing insights through an interactive web interface.

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

```text
health-insurance-predictor/
├── main.py                    # Streamlit web application entry point
├── premium_estimator.py       # Core prediction engine & preprocessing pipeline
├── visual_elements.py         # Custom CSS and HTML styling functions
├── artifacts/                 # Serialized model data
│   ├── model_data_for_young.joblib
│   └── model_data_for_adults.joblib
├── notebooks/                 # Jupyter Notebooks
│   ├── First draft.ipynb
│   ├── ml premium project adults with gr.ipynb
│   ├── ml premium project young with gr.ipynb
│   ├── ml premium project young.ipynb
│   └── Segmenting dataset.ipynb
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🛠️ Data Processing Pipeline

1. **Data Cleaning & Outlier Handling:** Processed an initial dataset of 50,000 records. Applied domain logic to remove impossible age values and utilized a 99.9th percentile threshold to appropriately handle extreme income outliers without losing critical high-net-worth data.

2. **Feature Engineering:** Converted ordinal categories (such as Plan Tier and Income Level) into numerical values and utilized one-hot encoding for nominal variables (such as Region and Smoking Status). Evaluated Variance Inflation Factors (VIF) to detect and resolve multicollinearity.

3. **Model Selection:** Evaluated multiple algorithms (Linear Regression, Ridge, Lasso, and XGBoost) and utilized `RandomizedSearchCV` for hyperparameter tuning to ensure optimal model performance before serialization.

## 🚀 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/health-insurance-predictor.git
cd health-insurance-predictor
```

2. **Install dependencies:**
Ensure you have Python 3.8+ installed. Install the required packages via `requirements.txt`:
```bash
pip install -r requirements.txt
```
(Required packages include `streamlit`, `pandas`, `scikit-learn`, `xgboost`, and `joblib`).

3. **Run the Streamlit App:**
```bash
streamlit run main.py
```
The application will launch automatically in your default web browser.
