import streamlit as st
import EDA
import predict

st.set_page_config(
    layout = 'wide',
    initial_sidebar_state='expanded',
    page_title='FIFA 2022'
)

page = st.sidebar.selectbox('Pilih halaman', ('EDA','predict'))
if page == 'EDA':
    EDA.run()
else:
    predict.run()