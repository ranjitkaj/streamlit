import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import graphviz



a = graphviz.Graph(engine='neato')
a.edge('Source','process')
a.edge('process','Source')
a.edge('process','output')
a.edge('output','Source')
st.graphviz_chart(a)




df = pd.read_csv("penguins.csv")
df1=df.drop(['Unnamed: 0'], axis=1)

st.title("My streamlit web app")
st.write("This is the raw dataset")
st.write(df1)
st.write("Data Description")
st.write(df1.describe())

st.write("Data Info")
st.write(df1.info())

st.write("Bar Plot")

st.code('st.write("Plot") fig = plt.figure(figsize = (19, 10)) plt.bar(df["island"], df["bill_length_mm"], color="blue" plt.xlabel("island") plt.ylabel("bill_length_mm") plt.title("Matplotlib Bar Chart") st.pyplot(fig)')
fig = plt.figure(figsize = (19, 10))

plt.bar(df['island'], df['bill_length_mm'], color='blue')

plt.xlabel('island')

plt.ylabel('bill_length_mm')

plt.title('Matplotlib Bar Chart ')

st.pyplot(fig)



st.write("Scatter Plot")
st.code("fig1 = plt.figure(figsize = (19, 10)) plt.scatter(df['island'], df['bill_length_mm'], color='c') plt.xlabel('island' plt.ylabel('bill_length_mm') plt.title('Matplotlib Bar Chart ') st.pyplot(fig1)")
fig1 = plt.figure(figsize = (19, 10))

plt.scatter(df['island'], df['bill_length_mm'], color='c')

plt.xlabel('island')

plt.ylabel('bill_length_mm')

plt.title('Matplotlib Bar Chart ')

st.pyplot(fig1)


st.line_chart(x='bill_length_mm', y='flipper_length_mm', data=df1)



sns.pairplot(df1)
sns.lineplot(x='bill_length_mm', y='bill_depth_mm',hue='island', data=df1, style='island', palette='cool',
             markers=['o','*','>'] , legend=False)








st.radio('Gender',['Female','Male'])


df2 = pd.read_csv('tips.csv')
fig = plt.figure(figsize=(5,5))
plt.scatter(df1['island'], df1['bill_depth_mm'])
st.pyplot(fig)



sns.pairplot(df2,hue='sex',kind='hist')
plt.show()






st.header('Designed By')

st.subheader('Ranjit Kumar')














