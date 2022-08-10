# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:48:10 2022

@author: Anusha Raj
"""
import pandas as pd
# file_name = pd.read_csv('file.csv') <---- format of read_csv
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data 
data.info()

#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding new column to data frame

data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

# Rounding Markup
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# Combining Data Fields

day = data['Day'].astype(str)
year = data['Year'].astype(str)
my_date = day+'-'+ data['Month'] + '-' + year
data['date'] = my_date


# using iloc to view specific columns/row
data.iloc[0] #views the row with the index=0
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows

data.head(5) #brings in first 5 rows

#brings in all rows of the 2nd column
data.iloc[:,2]

#fourth row, second column
data.iloc[4,2]

# using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new colums for the split colums in the Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

















