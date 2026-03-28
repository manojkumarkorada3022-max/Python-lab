import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [80, 90, 70]
}

df = pd.DataFrame(data)

print("Sorted Data:")
print(df.sort_values('Marks'))

print("\nFirst 2 rows:")
print(df.head(2))