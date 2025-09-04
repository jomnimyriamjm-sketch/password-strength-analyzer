import pandas as pd

file_path = "../data/raw/top10k.txt"
passwords = pd.read_csv(file_path, names=["password"])
print(passwords.head())
