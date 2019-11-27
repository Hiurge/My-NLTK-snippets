'''
1 In order to provide quality servi
'''

'''
2 In order to provide quality servi'''


'''3 In order to provide quality servi'''


'''4 In
 order to quality 
servi'''


import pandas as pd

path = '/home/luke/Downloads/DATASETS/BIG5/data.csv'
df = pd.read_csv(path, sep='\t', )
df.source = df.source.replace('url', 4) #  2=from google, 3=from facebook, 4=from any url
df.source = df.source.replace('facebook', 3) #  2=from google, 3=from facebook, 4=from any url
df.source = df.source.replace('#google', 2) #  2=from google, 3=from facebook, 4=from any url
df.source = df.source.replace('#google', 2)
df.source = df.source.replace('#google', 2) 

questions = df.columns[7:]
#questions
df

#1=test website 6=other