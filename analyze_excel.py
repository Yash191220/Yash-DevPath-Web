
import pandas as pd
import json

try:
    # Read with header at row 1 (index 1) - judging by previous output having "0" and "1" as likely row indices before header
    # Adjust as needed. I'll read simpler this time.
    df = pd.read_excel('HaclFiesta-Rankings.xlsx')
    
    # helper to find header
    header_idx = -1
    for i, row in df.iterrows():
        # Look for "Rank" and "Total" in the same row
        vals = [str(v).lower() for v in row.values]
        if 'rank' in vals and 'total' in vals:
            header_idx = i + 1 # +1 because pandas range is 0-indexed relative to read data, but we want to reload with this as header
            break
            
    if header_idx != -1:
        # Reload with correct header
        df = pd.read_excel('HaclFiesta-Rankings.xlsx', header=header_idx)
    
    # Drop rows where "Total" is NaN
    df = df.dropna(subset=['Total'])
    
    # Get columns
    cols = df.columns.tolist()
    print("FINAL COLUMNS:", json.dumps(cols))
    
    # Get first 3 rows
    records = df.head(3).to_dict(orient='records')
    # Clean nans for json dump
    clean_records = []
    for r in records:
        clean_records.append({k: (v if pd.notna(v) else None) for k,v in r.items()})
        
    print("SAMPLE DATA:", json.dumps(clean_records, default=str))

except Exception as e:
    print("Error:", e)
