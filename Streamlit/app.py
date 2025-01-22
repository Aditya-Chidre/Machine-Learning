import streamlit as st
import pandas as pd
import numpy as np

# Title of app
st.title("Hello User")

# Create a dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'first column':[10,20,30,40]
})

# Display df
st.write("This is our data")
st.write(df)

# Line chart
chart = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart)
