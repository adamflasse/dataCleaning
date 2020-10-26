import re
import pandas as pd


lst = [1,2,3,4,6,7]

def findId(s):
    pattern = r'\d{7}'
    new_string = str(s)
    res = re.findall(pattern, s)
    return res[0]


df = pd.read_csv('/Users/adamflasse/Development/python/challenges/October/newDataframe.csv', sep=',')

result = pd.DataFrame()

for i in lst:
    new_df = df[df['source'] == i]
    if (i == 1 or i == 7):
        new_df['hyperlink'] = new_df['hyperlink'].apply(findId)
    result = result.append(new_df)

print(result.shape)
result = result.drop_duplicates(subset = 'hyperlink', keep='first')

print(result.shape)
result.to_csv('/Users/adamflasse/Development/python/challenges/October/updatedDataframe.csv')


