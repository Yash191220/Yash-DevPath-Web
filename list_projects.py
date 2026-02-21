
import pandas as pd
import json

try:
    df = pd.read_excel('HaclFiesta-Rankings.xlsx')
    # Find header
    header_idx = -1
    for i, row in df.iterrows():
        vals = [str(v).lower() for v in row.values]
        if 'rank' in vals and 'total' in vals:
            header_idx = i + 1
            break
            
    if header_idx != -1:
        df = pd.read_excel('HaclFiesta-Rankings.xlsx', header=header_idx)
        print("PROJECTS:", json.dumps(df['Projects'].dropna().astype(str).tolist()))
except Exception as e:
    print(e)
