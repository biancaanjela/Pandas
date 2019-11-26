import pandas as bi

cars = bi.read_csv ('cars.csv')

print (cars.loc[0:4], cars.loc[27:31])
