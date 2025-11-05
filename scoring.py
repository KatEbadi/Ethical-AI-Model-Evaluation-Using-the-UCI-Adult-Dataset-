def calculate_ethics_score(scores_dict):
    total = sum(float(v) for v in scores_dict.values())
    count = len(scores_dict)
    return round((total / count) * 5, 2)
