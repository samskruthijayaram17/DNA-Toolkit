import os
import pandas as pd
import matplotlib.pyplot as plt

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

    plt.figure(figsize=(10, 5))
    plt.bar(df["gene_id"], df["sample1"])
    plt.xlabel("Gene ID")
    plt.ylabel("Expression Level")
    plt.title("Gene Expression Levels")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.imshow(df[["sample1", "sample2"]], aspect="auto", cmap="Blues")
    plt.title("Gene Expression Heatmap")
    plt.yticks(range(len(df["gene_id"])), df["gene_id"])
    plt.colorbar()
    plt.show()
except Exception as e:
    print(f"Error: {e}")
