import pandas as pd
import streamlit as st
import pickle
from data_cleaning import result_dic, characteristics
from utils import clean_price_str


with open('models/model_sgd.pkl', 'rb') as file: #  <----- Choose your model by changing the file here
    trained_pipe = pickle.load(file)


brands_list = list(result_dic.keys())
brands_list.append("Other")


st.write("General informations :")
brand = (st.selectbox('Brand', brands_list)).lower()
if brand == 'other':
    new_brand = st.text_input("Brand")
    model = "other"

else:
    models = list(set(result_dic[brand]))
    models = sorted([x.lower() for x in models])
    models.append("other")
    model = st.selectbox('Model', models).lower()



if model == "other":
    new_model = st.text_input('Car model')
    st.write("Technic informations :")
    wheelbase = st.number_input("wheelbase (cm)")
    carlength = st.number_input("car length (cm)")
    carwidth = st.number_input("car width (cm)")
    carheight = st.number_input("car height (cm)")
    curbweight = st.number_input("car weight when empty (kg)")
    cylindernumber = st.select_slider("number of cylinders",["2 (bi-rotor)", 3, 4, 5, 6, 8, 10, 12])
    cylindernumber = 2 if type(cylindernumber)==str else cylindernumber
    enginesize = st.number_input("engine size (liters)")
    drivewheel = st.radio("engine location", ["fwd", "rwd", "4wd"])
    aspiration = "turbo" if st.checkbox("turbo") else "std"
    enginelocation = st.radio("engine location", ["front", "rear"])
    consumption = st.slider("Fuel Cnsumption (L/100km)", min_value=0, max_value=30)
    
else:
    dic = characteristics[model]
    wheelbase = dic["wheelbase"]
    carlength = dic["carlength"]
    carwidth = dic["carwidth"]
    carheight = dic["carheight"]
    curbweight = dic["curbweight"]
    cylindernumber = dic["cylindernumber"]
    enginesize = dic["enginesize"]
    drivewheel = dic["drivewheel"]
    aspiration = dic["aspiration"]
    enginelocation = dic["enginelocation"]
    consumption = dic['consumption']

st.write("Technic informations :")
fueltype = st.radio("Fuel :", ["gas", "diesel"])
doornumber = st.radio("Number of doors :", [2, 4])
horsepower = st.number_input("horsepowers")



if st.button("Estimate"):
    input = pd.DataFrame(data={
            "brand" : brand,
            "wheelbase" : wheelbase,
            "carlength" : carlength,
            "carwidth" : carwidth,
            "carheight" : carheight,
            "curbweight" : curbweight,
            "cylindernumber" : cylindernumber,
            "enginesize" : enginesize,
            "horsepower" : horsepower,
            "consumption" : consumption,
            "fueltype" : fueltype,
            "drivewheel" : drivewheel,
            "aspiration" : aspiration,
            "doornumber" : doornumber,
            "enginelocation" : enginelocation
            }, index=[0])#carbody,
    
    st.write(clean_price_str(trained_pipe.predict(input)[0]))
# trained_pipe.predict()