import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, np.nan, 22, 32],})

#chech mising values 
print(df.isnull())

#drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

#fill missing values with a specific value
df_filled = df.fillna({'Age': df['Age'].mean()})
print(df_filled)