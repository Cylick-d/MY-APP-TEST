import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_iris_dataset():
 iris = sns.load_dataset('iris')
 return iris
iris = load_iris_dataset()

ris = sns.load_dataset('iris')
st.write(iris.head()) 

species = st.selectbox(' Choose a species', iris['species'].unique())
filtered_data = iris[iris['species'] == species]
st.write(f'Displaying data for {species}:')
st.dataframe(filtered_data)

st.subheader(f'Scatter plot for {species}:')
sns.scatterplot(data=filtered_data, x='sepal_length', y='sepal_width', hue='species')
st.pyplot(plt.gcf())


