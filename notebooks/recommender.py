import pandas as pd

def get_recommendations(risk_appetite, perf_df, top_n=3):
    """
    Recommends top funds based on Sharpe Ratio for a given risk appetite.
    """
    risk_map = {
        'low': ['low', 'below average'],
        'moderate': ['moderate', 'average', 'above average'],
        'high': ['high', 'very high']
    }
    
    target = str(risk_appetite).strip().lower()
    allowed_grades = risk_map.get(target, [target])
    
    filtered = perf_df[perf_df['risk_grade'].astype(str).str.lower().isin(allowed_grades)].copy()
    
    if filtered.empty:
        filtered = perf_df[perf_df['risk_grade'].astype(str).str.lower() == target].copy()
        
    top_funds = filtered.sort_values(by='sharpe_ratio', ascending=False).head(top_n)
    
    cols = [c for c in ['scheme_name', 'risk_grade', 'sharpe_ratio', 'category', 'return_1yr'] if c in top_funds.columns]
    return top_funds[cols]
