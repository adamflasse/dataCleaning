import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use('seaborn')

# read csv file
df_outlier = pd.read_csv('/home/becode/Desktop/BXL-Bouman-2.22/data_vis/updated_1.csv')
# csv file with openfire column 
df_of = pd.read_csv('/home/becode/Desktop/BXL-Bouman-2.22/data_vis/updated_2.csv')


''' Z-score method to find the outliers in  price and rooms_number column 
It returns a list relational values in a range which can be compared. '''
z = np.abs(stats.zscore(df_outlier['price']))
z1 = np.abs(stats.zscore(df_outlier['rooms_number']))

'''This gives a list of indexes where the outlier is located'''
#print(np.where(z > 15))
#print(np.where(z1 > 30))

''' To drop all the outliers in price and rooms column '''
df_ofot = df_of.drop(df_of.index[3528])
df_ofot = df_of.drop(df_of.index[3680])
df_ofot = df_of.drop(df_of.index[6323])
df_ofot = df_of.drop(df_of.index[6660])
df_ofot = df_of.drop(df_of.index[6866])
df_ofot = df_of.drop(df_of.index[22675])
df_ofot = df_of.drop(df_of.index[24646])
df_ofot = df_of.drop(df_of.index[24647])
df_ofot = df_of.drop(df_of.index[25858])

''' Making different plots to show the relationship between various criterias '''

#creating a Heatmap on  all the numeric/boolean criterias 
sns.heatmap(df_outlier.corr(),annot = True, fmt='.1g', vmin=-1, vmax=1, center= 0,)

''' Applying lambda function to change the names in propety subtypes to lower case 
   and creating a bar plot on  propety subtypes and area '''
df_outlier['property_subtype']= df_outlier['property_subtype'].apply(lambda x : x.lower())
g =sns.barplot(x='property_subtype', y='area' , data =df_outlier, estimator = np.mean)
#formating the x axis ticks 
g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right',fontweight='light',
    fontsize='medium')

#creating a scatterplot on  rooms and area with a region legend 
sns.scatterplot(x='area', y='rooms_number', data=df_outlier, s= 50, hue = 'region')

#creating a relplot on garden and area  
sns.relplot(x="garden", y="area", data=df_outlier)

#creating a violinplot on region and area  
sns.violinplot(x=df_ofot['region'],y=df_ofot['area'])
plt.xticks(fontsize=14)
plt.xlabel('Region', fontsize=14)
plt.title('Relation between Region and area', fontsize=20)


''' Plots to show the relationship between open_fire column and price '''

sns.boxplot(x='open_fire' , y = 'price' , data = df_ofot )
sns.barplot(x='open_fire' , y = 'price' , data = df_ofot)

''' Plot to show the outliers in the price , rooms_number and age column '''
ax = sns.scatterplot(x='rooms_number', y='price', data=df_outlier, s= 500)
sns.scatterplot(x='area', y='price', data=df_outlier, s= 100)
plt.xlabel('area')
plt.ylabel('price')

#sns.pairplot(df_outlier)

plt.tight_layout()
plt.title('Correlation between variables')
plt.show()