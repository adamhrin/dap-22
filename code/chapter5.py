## https://courses.mooc.fi/org/uh-cs/courses/dap-22/chapter-5/pandas-part-3

# %%
import pandas as pd
wh = pd.read_csv("https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_2020/master/kumpula-weather-2017.csv")
#%%
wh3 = wh.rename(columns={"m": "Month", "d": "Day", "Precipitation amount (mm)" : "Precipitation", 
                         "Snow depth (cm)" : "Snow", "Air temperature (degC)" : "Temperature"})
wh3.head()
# %%
groups = wh3.groupby("Month")
groups
# %%
for key, group in groups:
    print(key, len(group))
# %%
groups.get_group(2) 
# %%
groups["Temperature"]

#%%
groups["Temperature"].mean()

#%%
wh4 = wh3.copy()
wh4.loc[wh4.Precipitation == -1, "Precipitation"] = 0
wh4.loc[wh4.Snow == -1, "Snow"] = 0
wh4.head()
# %%
wh4.groupby("Month")["Precipitation"].sum()
# %%
def myfilter(df):                                     # The filter function must return a boolean value
    return df["Precipitation"].sum() >= 150

wh4.groupby("Month").filter(myfilter)
# %%
def myfilter(df):                                     # The filter function must return a boolean value
    return df["Precipitation"].sum() >= 100

wh4.groupby("Month").filter(myfilter)
# %%
pd.concat([wh4.iloc[:, 0:3], 
           wh4.groupby("Month")[["Precipitation", "Snow", "Temperature"]].transform(lambda x : x - x.mean())], 
          axis=1)
# %%
wh4.groupby("Month").apply(lambda df : df.sort_values("Temperature"))
# %%
