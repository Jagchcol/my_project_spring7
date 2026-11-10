import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.read_csv("./vehicles_us.csv")
st.header("Ventas de Vehiculos Mensual")
if st.button("Ventas Mensuales"):
    fig= px.histogram( df, x="price")
    st.plotly_chart(fig, key="Price Month")
if st.button("Precio y año"):
    fig= px.scatter(df, x="price", y="model_year")
    st.plotly_chart(fig, key="Price Model")

