import joblib 
import pandas as pd 
 
def load_model(filepath): 
    return joblib.load(filepath) 
 
def load_test_data(path): 
    return pd.read_csv(path) 
