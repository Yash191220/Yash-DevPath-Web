
import pandas as pd

INPUT_FILE = 'HaclFiesta-Rankings.xlsx'

def print_headers():
    try:
        # Read first few rows to find header
        df_preview = pd.read_excel(INPUT_FILE, header=None, nrows=20)
        header_idx = -1
        
        for i, row in df_preview.iterrows():
            vals = [str(v).lower() for v in row.values]
            if 'rank' in vals and 'total' in vals:
                header_idx = i
                break
        
        if header_idx != -1:
            df = pd.read_excel(INPUT_FILE, header=header_idx)
            print("--- HEADERS FOUND ---")
            for col in df.columns:
                print(repr(col))
        else:
            print("Header row not found")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_headers()
