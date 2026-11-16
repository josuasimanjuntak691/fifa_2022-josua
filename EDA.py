import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image



def run():
    #membuat judul
    st.title('aplikasi prediksi rating pemain')
    # membuat sub header
    st.subheader('file ini berisi exploratory data analys')

    #menulis baris
    st.write('by *josua simanjuntak*')
    st.write('# hello')
    st.write('## hello')


    #memasukkan data
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.4/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    #memasukkan gambar
    img = Image.open('bola.jpg')
    st.image(img, caption="eda bola")

    #menampilkan histogram rating
    st.write('### histogram of rating')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df['Overall'],bins=30,kde=True)
    st.pyplot(fig)

    #membuat
    st.write('### histogram berdasarkan input user')
    fig = plt.figure(figsize=(15,5)) 
    opsi = st.selectbox('pilih column',('Weight','Height','ShootingTotal'))
    sns.histplot(df[opsi],bins=30,kde=True)
    st.pyplot(fig)

    #st.write('### plotly plot - rating vs price')
    #fig = px.scatter(df,x='Overall',y='ValueEUR')
    #st.plotly_chart(fig)



if __name__ == '__main__':
    run()    