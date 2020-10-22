import pandas as pd
import numpy as np

df = pd.read_csv('/home/becode/Desktop/BXL-Bouman-2.22/data_vis/updated.csv')

''' For removing the '.' in the postcode '''
df['postcode']= df['postcode'].apply(lambda x : str(x).split('.')[0])
df['postcode']= df['postcode'].astype(int)

'''Function to group the postcodes by province '''
def define_province(x):
    if ((x >= 1000) & (x < 1299)) :
        return 'Brussels Capital Region'
    elif ((x >= 1300) & (x < 1499)) :
        return 'Walloon Brabant'
    elif (((x >= 1500) & (x < 1999)) | ((x >= 3000) & (x < 3499))):
        return 'Flemish Brabant'
    elif ((x >= 2000) & (x < 2999)) :
        return 'Antwerp'
    elif ((x >= 3500) & (x < 3999)) :
        return 'Limburg'
    elif ((x >= 4000) & (x < 4999)) :
        return 'Liège'
    elif ((x >= 5000) & (x < 5999)) :
        return 'Namur'
    elif (((x >= 6000) & (x < 6599)) | ((x >= 7000) & (x < 7999))):
        return 'Hainaut'
    elif ((x >= 6600) & (x < 6999)) :
        return 'Luxembourg'
    elif ((x >= 8000) & (x < 8999)) :
        return 'West Flanders'
    elif ((x >= 9000) & (x < 9999)) :
        return 'East Flanders'
    elif (x > 10000) : 
        return 'more'

# Adding the province column to the dataframe 
df['province'] = df['postcode'].apply(define_province)

#Function to group provinces in to 3 regions
def define_reg(x):
    if (x == 'Brussels Capital Region') :
        return 'Brussels'
    elif ((x == 'Walloon Brabant') | (x == 'Liège') | (x == 'Namur') | (x == 'Hainaut') | (x == 'Luxembourg')) :
        return 'Wallonia'
    elif ((x == 'Flemish Brabant') | (x == 'Antwerp') | (x == 'Limburg') | (x == 'West Flanders') | (x == 'East Flanders')) :
        return 'Flanders'

# Adding the region column to the dataframe 
df['region'] = df['province'].apply(define_reg)

#Function to Combine the duplicate names in the condition column
def building_condition(x) :
    if ((x == 'AS_NEW') | (x == 'As new')| (x == 'Just renovated') | (x == 'JUST_RENOVATED')):
        return 'As New'
    elif ((x == 'To be done up') | (x == 'TO_BE_DONE_UP') | (x == 'To renovate') | (x == 'TO_RENOVATE') | (x == 'TO_RESTORE') | (x == 'To restore')) :
        return 'To be Renovated'
    elif ((x == 'Good') | (x == 'GOOD')) :
        return 'Good'
    else :
        return 'Not specified' 

#Updating the Building state column
df['building_state'] = df['building_state'].apply(building_condition)


#Cleaning the Price column in the dataframe
columns = ['price']
df = df.replace(0, np.nan).dropna(axis=0, how='any', subset=columns)
df = df.replace('None', np.nan).dropna(axis=0, how='any', subset=columns)

df['price']= df['price'].apply(lambda x : str(x).replace('€',' ').strip())
df['price']= df['price'].apply(lambda x : str(x).replace('.',''))
df['price']= df['price'].apply(lambda x : str(x).replace(',',''))
df['price'] = pd.to_numeric(df['price'])

#Cleaning the Area column in the dataframe
columns = ['area']
df = df.replace(0, np.nan).dropna(axis=0, how='any', subset=columns)
df = df.replace('None', np.nan).dropna(axis=0, how='any', subset=columns)
df['area'] = df['area'].apply(lambda x: str(x).strip().replace('m2 ',''))
df['area'] = pd.to_numeric(df['area'])


# to be double checked what columns have to be dropped
df = df.drop(df.columns[[0,1, 2, 3]], axis = 1)

df.to_csv(r'/home/becode/Desktop/BXL-Bouman-2.22/data_vis/updated_1.csv', index = False)