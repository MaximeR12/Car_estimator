import pandas as pd
from utils import convert_mpg_to_l_100km, convert_cubic_inches_to_liters, convert_pounds_to_kilograms, convert_to_centimeters,correct_brands, nb_str_to_int

df = pd.read_csv('carprice.csv')

df[['brand','model']] = df["CarName"].str.split(pat=" ", n=1, expand=True)

df = df.drop(['CarName', "car_ID"], axis = 1)

df["wheelbase"] = df["wheelbase"].apply(convert_to_centimeters)
df["carlength"] = df["carlength"].apply(convert_to_centimeters)
df["carwidth"] = df["carwidth"].apply(convert_to_centimeters)
df["carheight"] = df["carheight"].apply(convert_to_centimeters)

df['curbweight'] = df['curbweight'].apply(convert_pounds_to_kilograms)

df["enginesize"] = df["enginesize"].apply(convert_cubic_inches_to_liters)

df["cylindernumber"] = df["cylindernumber"].apply(nb_str_to_int)
df["doornumber"] = df["doornumber"].apply(nb_str_to_int)

df['brand'] = df["brand"].apply(correct_brands)

df["model"] = df["model"].replace(" (sw)", '').str.lower()

df["consumption"] = df[["citympg","highwaympg"]].mean(axis=1)
df.drop(["citympg", "highwaympg"], axis=1)
df['consumption'] = df['consumption'].apply(convert_mpg_to_l_100km)








df.to_csv('carprice_cleaned.csv')

result_dic = {key: list(group["model"]) for key, group in df.groupby("brand")}
#df_by_model = df.groupby(by='model')

characteristics ={}
for line in df.values:
    characteristics[line[25]] = {"wheelbase" : line[7],
                                "carlength" : line[8], 
                                "carwidth" : line[9], 
                                "carheight" : line[10],
                                "curbweight" : line[11],
                                "cylindernumber" : line[13],
                                "enginesize" : line[14],
                                "drivewheel" : line[5],
                                "aspiration" : line[2],
                                "enginelocation" : line[6],
                                "consumption" : line[26]
                                }
    