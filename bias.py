import numpy as np 
 
def analyze_bias_distribution(model, X_test, y_test): 
    predictions = model.predict(X_test) 
    return { 
        "prediction_mean": np.mean(predictions), 
        "true_mean": np.mean(y_test), 
        "bias_score": np.abs(np.mean(predictions) - np.mean(y_test)) 
    }
