import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('https://github.com/cvermno/ML-Project/raw/main/Datasets/training_data.csv')

# Streamlit app
st.title('Le Petit Prof')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

# Create a pie chart using Plotly Express
fig = px.pie(data, names='difficulty', values='count', title='French sentences sorted by difficulty')

# Display the pie chart using Streamlit
st.plotly_chart(fig)
st.write("#Is French a difficult language to learn?")
st.write(training)
