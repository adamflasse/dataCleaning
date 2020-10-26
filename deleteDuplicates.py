import pandas as pd


url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'
df = pd.read_csv(url, sep=',')

result = pd.DataFrame()

for i in range(7):
    if i == 1 or i == 3:
        continue
    new_df = df[df['source'] == i+1]
    new_df = new_df.drop_duplicates(subset = 'hyperlink', keep='first')
    result = result.append(new_df)


print(result.shape)
result.to_csv('/Users/adamflasse/Development/python/challenges/October/newDataframe.csv', header = True)

