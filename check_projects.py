
import pandas as pd
try:
    df = pd.read_excel('HaclFiesta-Rankings.xlsx')
    # search whole dataframe for "Apex"
    print("Contains Apex?", df.apply(lambda x: x.astype(str).str.contains('Apex', case=False).any()).any())
    
    # print all values in "Projects" column if it exists or column 1
    # Re-detect header logic quickly
    header_idx = -1
    for i, row in df.iterrows():
        vals = [str(v).lower() for v in row.values]
        if 'rank' in vals and 'total' in vals:
            header_idx = i + 1
            break
    
    if header_idx != -1:
        df = pd.read_excel('HaclFiesta-Rankings.xlsx', header=header_idx)
        if 'Projects' in df.columns:
            print("Projects:", df['Projects'].dropna().tolist())
except Exception as e:
    print(e)
