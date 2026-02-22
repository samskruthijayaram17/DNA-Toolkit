import pandas as pd
import os
def find_csv_file(filename="gene_expression.csv"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Search in examples folder and sibling data folder
    search_paths = [
        os.path.join(script_dir, "examples", filename),
        os.path.join(script_dir, "..", "data", filename),
        os.path.join(script_dir, "data", filename),
        os.path.join(script_dir, "..", "..", "data", filename)
    ]
    
    for path in search_paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"{filename} not found in search paths.")

try:
    csv_file = find_csv_file()
    print(f"Loading data from: {csv_file}")
    df = pd.read_csv(csv_file)
    high_expression = df[df["sample1"] > 10] 
    print("\nHigh expression genes:")
    print(high_expression)
    print("\nImportant gene:")
    for gene in high_expression["gene_id"]:
        print(gene)
except Exception as e:
    print(f"Error: {e}")