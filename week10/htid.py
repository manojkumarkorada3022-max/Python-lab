import pandas as pd
df = pd.read_csv('C:\\24331A05E6\\week10\\data.csv')

print("Head (first 5 rows):")
print(df.head())

print("\nTail (last 5 rows):")
print(df.tail())

print("\nInfo:")
df.info()

print("\nDescribe:")
print(df.describe())