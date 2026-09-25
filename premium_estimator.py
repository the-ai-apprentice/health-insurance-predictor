import pandas as pd
import joblib
import sklearn


set_under_25 = joblib.load("artifacts/model_data_for_young.joblib")
set_over_25 = joblib.load("artifacts/model_data_for_adults.joblib")

def preprocessing_data(input_dict):
    input_df = pd.DataFrame([input_dict])
    if input_dict['age'] <= 25:
        model_data = set_under_25
    else:
        model_data = set_over_25

    #1. calculating total_risk_score
    medical_history = input_dict['medical_history']
    total_risk_score = 0

    for disease in medical_history:
        total_risk_score += model_data['risk_scores'].get(disease.lower(), 0)

    input_df['total_risk_score'] = total_risk_score
    input_df['disease_1'] = "a"
    input_df['disease_2'] = "b"

    # 2. Calculating normalized risk score
    input_df['normalized_risk_score'] = model_data['risk_scaler'].transform(input_df[['total_risk_score']])

    # 3. Ordinal encoding
    input_df[model_data['ordinal_cols']] = model_data['ordinal_encoder'].transform(input_df[model_data['ordinal_cols']])

    # 4. Nominal (one-hot) encoding
    input_df[model_data['new_nominal_cols']] = model_data['nominal_encoder'].transform(input_df[model_data['nominal_cols']])

    # 5. Drop the initial redundant columns
    x_input = input_df.drop(model_data['cols_to_drop'], axis="columns")

    # 6. Scale the numerical columns
    x_input[model_data['cols_to_scale']] = model_data['scaler'].transform(x_input[model_data['cols_to_scale']])

    # 7. Drop the 'income_level' to match VIF reduction
    x_input = x_input.drop("income_level", axis="columns")

    # 8. Ensuring the column order perfectly matches the training data
    return x_input[model_data['final_columns']], model_data['best_model']

def predict_amount(input_dict):
    x_processed, model = preprocessing_data(input_dict)
    amount = model.predict(x_processed)[0]
    return round(amount, 2)

