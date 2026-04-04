import pandas as pd
data={

    "Name":["Alice","Bob","Charlie","David"],
    "Age":[25,30,45,67],
    "City":['New York','Los Angeles','Chicago','Houstan']

}
df=pd.DataFrame(data)
print("Data:")
print(df)
print("\nDataFrame Information:")
print(df.info())

Series=pd.Series(data)
print("\nSeries:")
print(Series)