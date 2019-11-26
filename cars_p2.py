import pandas as bi

cars = bi.read_csv ('cars.csv')

print ("\n","a.)","\n",cars.loc[0:4,['Model','cyl','hp','wt','vs','gear']])
print ("\n","b.)","\n",cars.loc[0,'Model'])
print ("\n","c.)","\n",cars.loc[22,'cyl'])
print ("\n","d.)","\n",cars.loc[[1,18,28],['cyl','gear']])