import pandas as pd

# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [24, 27, 22, 32]}
# df = pd.DataFrame(data,index=['a', 'b', 'c', 'd'])

# print(df)

# s = pd.Series([10, 20, 30, 40])
# print(s)
# print(s[2])


data2 = {'name ': ['Alice', 'Bob', 'Charlie', 'David'],
        'marks': [85, 90, 78, 92]}

df2 = pd.DataFrame(data2)
df2.to_csv('output.csv', index=False)
# print(df2)      
# # print(df2['name '])
# # print(df2['marks'])


# df = pd.DataFrame({
#         'A': [1, 2, 3],
#         'B': [4, 5, 6],
#         'C': [7, 8, 9]
#     })
# # print(df)
# # print(df['A'])

# # print(df.loc[1])

# # print(df.iloc[0:1])

# print(df[df['C']>7])
# # print(df.l)

# #adding a new column
# df['D'] = df['A'] + df['B'] + df['C']
# print(df)


# #Replacing a column
# df['C'] =df['A'] + df['B']
# print(df)

# #update a value 
# df.loc[1, 'B'] = 10
# print(df)


# #drop column 
# df = df.drop('C', axis=1)
# print(df)

# df = df.drop(0, axis=0)
# print(df)


# #rename column 
# df = df.rename(columns={'A': 'Alpha', 'B': 'Beta', 'D': 'Delta'})
# print(df)


# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [24, 27, 22, 32]}
# df = pd.DataFrame(data)
# #filer age>30 
# print(df[df['age']>30])

# #multiple conditions
# print(df[(df['age']>25) & (df['age']< 40)])

# print(sorted(df['age']))

# print(df.sort_values('age'))
# print(df.sort_values('age', ascending=False))



# df3 = pd.DataFrame({
#          'Team': ['A', 'B', 'A', 'B', 'A', 'B'],
#          'Score': [10, 15, 14, 10, 18, 20]
#      })
# print(df3.groupby('Team').sum())


# df4 = pd.DataFrame({'A': [1, 2, 3, 4]}, index=['a', 'b', 'c', 'e'])
# df5 = pd.DataFrame({'B': [5, 6, 7, 8]}, index=['a', 'b', 'c', 'd'])

# print(df4.join(df5))

# # df6 = pd.DataFrame({'A': [1, 2, 3, 4]})
# # df7 = pd.DataFrame({'A': [3, 4, 5, 6]})

# print(pd.concat([df4, df5], axis=1))
# # print(pd.concat([df6, df7], axis=1))


# df8 = pd.DataFrame({
#        'Date': ['2025-01-01', '2025-02-10', '2025-03-15']
# })

# df8['Date'] = pd.to_datetime(df8['Date'])
# print(df8['Date'].dt.month)
# print(df8['Date'].dt.date)

# print(df8[df8['Date']> '2025-02-01'])


#read csv file
df = pd.read_csv('csvfile.csv')
print(df)

df2 = pd.read_csv('output.csv')
print(df2) 


df3 = pd.read_json('jsonfile.json')
print(df3)