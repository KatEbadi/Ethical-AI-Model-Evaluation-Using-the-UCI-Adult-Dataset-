import numpy as np
import shap

def generate_shap_values(model, X_test): 
    explainer = shap.Explainer(model)
    # Sample only 100 rows to make SHAP faster
    return explainer(X_test.sample(n=100, random_state=42)) 

def compute_transparency_score(shap_values):
    # Extract absolute SHAP values (NumPy array)
    abs_values = np.abs(shap_values.values)  # shape: (samples, features, classes)
    
    # Sum over samples (axis=0), resulting shape: (features, classes)
    importance_per_class = abs_values.sum(axis=0)
    
    # Sum over classes (axis=1), resulting shape: (features,)
    importance = importance_per_class.sum(axis=1)
    
    # Normalize importance so sum=1
    normalized = importance / importance.sum()
    
    # Max normalized importance (scalar)
    max_val = normalized.max()
    
    # Transparency score = 1 - max_val
    score = 1.0 - max_val
    
    # Return as float (plain Python float)
    return float(score)
