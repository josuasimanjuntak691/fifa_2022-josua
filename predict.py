import pickle
import json
import pandas as pd
import numpy as np
import streamlit as st

# Load all files

with open('model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)


def run():
  with st.form('fifa 2022'):
    name = st.text_input('name',value='')
    age = st.number_input('age',min_value=15, max_value=40, step=1, help="usia pemain")
    weight = st.number_input('Weight', min_value=60, max_value=100,value=80)
    height = st.slider('Height', min_value=150, max_value=230, value=180)
    price = st.number_input('price',min_value=0,max_value=1000000000,value=0)
    st.markdown('---')

    attacking_work_rate = st.selectbox('attacking work rate', ('low','medium','high'))
    defensive_work_rate = st.radio('defensive work rate', ('low','medium','high'))
    st.markdown('---')

    pace = st.number_input('pace',min_value=0,max_value=100,value=50)
    shooting = st.number_input('shooting',min_value=0,max_value=100,value=50)
    passing = st.number_input('passing',min_value=0,max_value=100,value=50)
    dribbling = st.number_input('dribbling',min_value=0,max_value=100,value=50)
    defending = st.number_input('defending',min_value=0,max_value=100,value=50)
    physicality = st.number_input('physicality',min_value=0,max_value=100,value=50)
 
    submitted = st.form_submit_button('predict')
  # Create a new data
  # Use all columns not just the results of feature selection

  data_inf = {
    'Name': name,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Price': price,
    'AttackingWorkRate': attacking_work_rate,
    'DefensiveWorkRate': defensive_work_rate,
    'PaceTotal': pace,
    'ShootingTotal': shooting,
    'PassingTotal': passing,
    'DribblingTotal': dribbling,
    'DefendingTotal': defending,
    'PhysicalityTotal':physicality
    }

  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)
  if submitted:
    data_inf_num = data_inf[list_num_cols]
    data_inf_cat = data_inf[list_cat_cols]

    data_inf_num_scaled = model_scaler.transform(data_inf_num)
    data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
    data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

    y_pred_inf=model_lin_reg.predict(data_inf_final)
    st.write('# rating :', str(int(y_pred_inf[0])))
if __name__ == '__main__':
  run()