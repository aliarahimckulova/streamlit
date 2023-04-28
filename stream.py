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


df = df.drop(columns=['Отметка времени'])

st.title("What environmental issues do you think are the most important?")
question = st.selectbox("What environmental issues do you think are the most important?", df.columns)
answers = df[question].str.split(", ")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
#fig = go.Figure(go.Bar(x=answer_counts.index, y=answer_counts.values, orientation='h'))
fig = go.Figure()
fig.add_trace(go.Bar(x=answer_counts.values,
                     y=answer_counts.index,
                     orientation='h',
                     text=answer_counts.values,
                     textposition='outside',
                     marker=dict(color='rgba(50, 171, 96, 0.6)',
                                 line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))
fig.update_layout(title=f"Number of selected answers for {'What environmental issues do you think are the most important?'}",
                  xaxis_title="Answer",
                  yaxis_title="Count")
st.plotly_chart(fig)

st.title("Where do you get information about the current environmental situation?")
question = st.selectbox("Where do you get information about the current environmental situation?", df.columns)
answers = df[question].str.split(", ")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
#fig = go.Figure(go.Bar(x=answer_counts.index, y=answer_counts.values, orientation='h'))
fig = go.Figure()
fig.add_trace(go.Bar(x=answer_counts.values,
                     y=answer_counts.index,
                     orientation='h',
                     text=answer_counts.values,
                     textposition='outside',
                     marker=dict(color='rgba(50, 171, 96, 0.6)',
                                 line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))
fig.update_layout(title=f"Number of selected answers for {'Where do you get information about the current environmental situation?'}",
                  xaxis_title="Answer",
                  yaxis_title="Count")
st.plotly_chart(fig)


st.title("Do you lead an eco-friendly lifestyle?")
question = st.selectbox("Do you lead an eco-friendly lifestyle?", df.columns)
answers = df[question].dropna()
answer_counts = answers.value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Do you lead an eco-friendly lifestyle?'}'")
st.plotly_chart(fig)

import re

st.title("What is the main motivation for you to lead an ecological lifestyle?")
question = st.selectbox("What is the main motivation for you to lead an ecological lifestyle?", df.columns)
answers = df[question].apply(lambda x: re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', x))
answer_counts = pd.Series()
for ans in answers:
    answer_counts = answer_counts.add(pd.Series(ans).value_counts(), fill_value=0)
answer_counts = answer_counts.sort_values(ascending=True)
fig = go.Figure()
fig.add_trace(go.Bar(x=answer_counts.values,
                     y=answer_counts.index,
                     orientation='h',
                     text=answer_counts.values,
                     textposition='outside',
                     marker=dict(color='rgba(50, 171, 96, 0.6)',
                                 line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))
fig.update_layout(title=f"Number of selected answers for '{'What is the main motivation for you to lead an ecological lifestyle?'}'",
                  xaxis_title="Answer",
                  yaxis_title="Count")
st.plotly_chart(fig)


st.title("What aspects of maintaining an ecological lifestyle are the most difficult for you?")
question = st.selectbox("What aspects of maintaining an ecological lifestyle are the most difficult for you?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
#fig = go.Figure(go.Bar(x=answer_counts.index, y=answer_counts.values, orientation='h'))
fig = go.Figure()
fig.add_trace(go.Bar(x=answer_counts.values,
                     y=answer_counts.index,
                     orientation='h',
                     text=answer_counts.values,
                     textposition='outside',
                     marker=dict(color='rgba(50, 171, 96, 0.6)',
                                 line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))
fig.update_layout(title=f"Number of selected answers for {'What aspects of maintaining an ecological lifestyle are the most difficult for you?'}",
                  xaxis_title="Answer",
                  yaxis_title="Count")
st.plotly_chart(fig)

st.title("Which of the following ideas do you think are the most useful?")
question = st.selectbox("Which of the following ideas do you think are the most useful?", df.columns)
answers = df[question].str.split(", ")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
#fig = go.Figure(go.Bar(x=answer_counts.index, y=answer_counts.values, orientation='h'))
fig = go.Figure()
fig.add_trace(go.Bar(x=answer_counts.values,
                     y=answer_counts.index,
                     orientation='h',
                     text=answer_counts.values,
                     textposition='outside',
                     marker=dict(color='rgba(50, 171, 96, 0.6)',
                                 line=dict(color='rgba(50, 171, 96, 1.0)', width=1))))
fig.update_layout(title=f"Number of selected answers for {'Which of the following ideas do you think are the most useful?'}",
                  xaxis_title="Answer",
                  yaxis_title="Count")
st.plotly_chart(fig)

st.title("How often do you recycle?")
question = st.selectbox("How often do you recycle?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'How often do you recycle?'}'")
st.plotly_chart(fig)

st.title("Do you use reusable bags when shopping?")
question = st.selectbox("Do you use reusable bags when shopping?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Do you use reusable bags when shopping?'}'")
st.plotly_chart(fig)

st.title("Have you installed energy-efficient lighting in your home (LED bulbs)?")
question = st.selectbox("Have you installed energy-efficient lighting in your home (LED bulbs)?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Have you installed energy-efficient lighting in your home (LED bulbs)?'}'")
st.plotly_chart(fig)

st.title("How often do you walk, bike, or take public transportation instead of driving a car?")
question = st.selectbox("How often do you walk, bike, or take public transportation instead of driving a car?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'How often do you walk, bike, or take public transportation instead of driving a car?'}'")
st.plotly_chart(fig)


st.title("Have you reduced your meat consumption or adopted a vegetarian/vegan diet?")
question = st.selectbox("Have you reduced your meat consumption or adopted a vegetarian/vegan diet?", df.columns)
answers = df[question].dropna()
answer_counts = answers.value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Have you reduced your meat consumption or adopted a vegetarian/vegan diet?'}'")
st.plotly_chart(fig)


st.title("Do you compost your food waste or use a composting service?")
question = st.selectbox("Do you compost your food waste or use a composting service?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Do you compost your food waste or use a composting service?'}'")
st.plotly_chart(fig)

st.title("Have you taken any steps to reduce your overall consumption, such as by buying fewer new products or participating in a buy nothing challenge?")
question = st.selectbox("Have you taken any steps to reduce your overall consumption, such as by buying fewer new products or participating in a buy nothing challenge?", df.columns)
answers = df[question].dropna()
answer_counts = answers.value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Have you taken any steps to reduce your overall consumption, such as by buying fewer new products or participating in a buy nothing challenge?'}'")
st.plotly_chart(fig)

st.title("Do you buy products made from sustainable materials, such as bamboo or organic cotton?")
question = st.selectbox("Do you buy products made from sustainable materials, such as bamboo or organic cotton?", df.columns)
answers = df[question].str.split(",")
answer_counts = pd.Series(sum(answers, [])).value_counts().sort_values(ascending=True)
fig = go.Figure(go.Pie(values=answer_counts.values, labels=answer_counts.index))
fig.update_layout(title=f"Number of selected answers for '{'Do you buy products made from sustainable materials, such as bamboo or organic cotton?'}'")
st.plotly_chart(fig)

st.title("Would you like to know more about environmental issues?")
values = df_main['Would you like to know more about environmental issues?'].value_counts()
keys = df_main['Would you like to know more about environmental issues?'].unique()
fig = go.Figure(go.Pie(values=values, labels=keys, hole=0.3, name="Count of answers"))
st.plotly_chart(fig)

st.title("Open questions")
df_open = df.iloc[:, -3:]
if st.checkbox('Open questions'):
    st.write(df_open)
