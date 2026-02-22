import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dna toolkit/data/gene_expression.csv")
print("\nData Overview:")
print(df.head())
print("Number of genes:", len(df))
average_expression = df["sample1"].mean()
print("\nAverage Expression Level:", average_expression)
print("Highest expression:", df["sample1"].max())
print("Lowest expression:", df["sample1"].min())
highly_expressed_genes = df[df["sample1"] > 10]
print("\nHighly Expressed Genes:")
print(highly_expressed_genes)
plt.bar(df["gene_id"], df["sample1"])
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.xticks(rotation=45)
plt.show()