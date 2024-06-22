import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Exploratory Data Analysis")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header("Data Preview")
    st.dataframe(df)

    st.header("Unique Values in Each Column")
    for column in df.columns:
        st.subheader(f"Unique values in column: {column}")
        unique_values = df[column].unique()
        st.write(unique_values)
        st.header("Visualizations")
        st.subheader("Select columns to visualize")
        columns = df.columns.tolist()
        selected_x = st.selectbox("Select X-axis column", columns)
        selected_y = st.selectbox("Select Y-axis column", columns)
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[selected_x], y=df[selected_y], ax=ax)
        st.pyplot(fig)