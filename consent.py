def check_consent_traceability(logs): 
    if 'consent_id' in logs.columns and logs['consent_id'].notnull().all(): 
        return 1.0 
    return 0.0
