import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Load data
df = pd.read_csv('Sustainable Lifestyle Questionnaire for App.csv')

# Extract main columns
df_main = df.iloc[:, 3:-3]

st.title("**♻️**Explore questionnare dashboard")
st.write("Here, you can see the demo of a simple web-app dashboard."
         "It will show you general information such as users answers for a specific ")

if st.checkbox('Show data'):
    st.write(df_main)
st.title("How many people are interested in environmental issues?")
values = df_main['Would you like to know more about environmental issues?'].value_counts()
keys = df_main['Would you like to know more about environmental issues?'].unique()

fig = go.Figure(go.Pie(values=values, labels=keys, hole=0.3))

st.plotly_chart(fig)
