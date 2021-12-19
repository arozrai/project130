import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)

del df ["Radius"]
print(df.shape)
del df ["Orbitial_period"]
del df ["Semimajor_axis"]
del df ["Ecc"]

print(df.shape)

print(list(df))

df = df.rename({
    "Distance":"Light_years_from_earth",
    "Star":"Name"
},axis="columns")

print(list(df))