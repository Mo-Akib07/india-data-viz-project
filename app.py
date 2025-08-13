import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout= "wide")

df = pd.read_csv("india.csv")
list_of_states = list(df["State"].unique())
list_of_states.insert(0, "Overall India")


st.sidebar.title("Data Visualization Of India")
selected_state = st.sidebar.selectbox("Select a State", list_of_states)

primary = st.sidebar.selectbox("Select Primary perameter", sorted(df.columns[1:]))
secondary = st.sidebar.selectbox("Select Secondary perameter", sorted(df.columns[1:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represents primary perameter")
    st.text("Color represents secondary perameter")
    if selected_state == "Overall India":
        # plot for india
        fig = px.scatter_mapbox(df, lat = "Latitude", lon= "Longitude", zoom= 4, mapbox_style= "carto-positron", size= primary, color= secondary, size_max=35, width=1500, height=800, hover_name= "District")
        
        st.plotly_chart(fig, use_container_width= True)
    else:
        # plot for state
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(state_df, lat = "Latitude", lon= "Longitude", zoom= 6, mapbox_style= "carto-positron", size= primary, color= secondary, size_max=35, width=1500, height=800, hover_name= "District")
        
        st.plotly_chart(fig, use_container_width= True)

