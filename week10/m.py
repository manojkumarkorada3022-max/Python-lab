import pandas as pd


df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [80, None, 70]
})

df['Result'] = ['Pass', 'Fail', 'Pass']

print(df)