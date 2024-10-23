import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder



data = pd.DataFrame({'gender' : ['male' , 'female' , 'non binary'],
                     'height' : ['short' , 'medium' , 'tall']})
                     
print(data)

ordinal_encoding1 = {'short' :1 , 'medium' : 2 , 'tall' : 3 }
data['height_encoding'] = data['height'].map(ordinal_encoding1)

print(data)

