import pandas as pd
x={"math":80,"Science":85,"English":80}
y=pd.Series(x)
print(y)
print(y['Science'])
print(y[y>80])
print("English:",y['English'])