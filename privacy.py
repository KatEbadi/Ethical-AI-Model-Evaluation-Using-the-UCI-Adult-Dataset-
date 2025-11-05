def estimate_privacy_risk(dataset): 
    risk_score = 0 
    sensitive_columns = ['age', 'gender', 'zipcode'] 
    for col in sensitive_columns: 
        if col in dataset.columns: 
            unique_vals = dataset[col].nunique() 
            risk_score += 1.0 / (unique_vals + 1) 
    return risk_score / len(sensitive_columns) 
