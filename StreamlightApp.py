import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.title("Dataset visualization and hypothesis testing")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded dataset:")
    st.write(df.head())

    # Dropdown to select two variables
    variables = df.columns.tolist()
    variable1 = st.selectbox("Select the first variable", variables)
    variable2 = st.selectbox("Select the second variable", variables)

    # Dropdown to select visualization type
    visualization_type = st.selectbox("Select visualization type", ["Histogram", "Pie Chart"])

    # Visualization of variable distributions
    st.write("Distribution of", variable1)
    if visualization_type == "Pie Chart" and df[variable1].dtype == "object":
        plt.figure(figsize=(8, 6))
        df[variable1].value_counts().plot(kind="pie")
        st.pyplot()
    else:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=variable1, kde=True)
        st.pyplot()

    st.write("Distribution of", variable2)
    if visualization_type == "Pie Chart" and df[variable2].dtype == "object":
        plt.figure(figsize=(8, 6))
        df[variable2].value_counts().plot(kind="pie")
        st.pyplot()
    else:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=variable2, kde=True)
        st.pyplot()

    # Dropdown to select hypothesis test
    test_options = ["T-Test", "Wilcoxon Rank-Sum Test"]
    selected_test = st.selectbox("Select a hypothesis test", test_options)

    # Perform hypothesis test and display results
    st.write("Results of", selected_test)

    if selected_test == "T-Test":
        t_statistic, p_value = stats.ttest_ind(df[variable1], df[variable2])
    else:
        t_statistic, p_value = stats.ranksums(df[variable1], df[variable2])

    st.write("T-Statistic:", t_statistic)
    st.write("P-Value:", p_value)

    alpha = 0.05
    if p_value < alpha:
        st.write("Reject the null hypothesis")
    else:
        st.write("Fail to reject the null hypothesis")
else:
    st.write("Upload a CSV file to get started")
