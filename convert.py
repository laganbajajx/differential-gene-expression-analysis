import pyreadr
import pandas as pd

result = pyreadr.read_r("leukemia_data_Golub99_3051.rda")

X_train = result["golub_train_3051"]
y_train = result["golub_train_response"]

X_test = result["golub_test_3051"]
y_test = result["golub_test_response"]

# Convert labels to 1D
y_train = y_train.iloc[:, 0]
y_test = y_test.iloc[:, 0]

# Add target
X_train["target"] = y_train.values
X_test["target"] = y_test.values

# Combine
df = pd.concat([X_train, X_test], ignore_index=True)

# Save
df.to_csv("gene_expression_final.csv", index=False)

print(df.shape)
print(df["target"].value_counts())
print("gene_expression_final.csv created successfully!")
