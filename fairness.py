def compute_fairness_score(model, X_test, y_test, demographics): 
    predictions = model.predict(X_test) 
    scores = {} 
    for group in demographics.unique(): 
        idx = demographics == group 
        group_outcomes = predictions[idx] 
        scores[group] = group_outcomes.mean() 
    return scores 
