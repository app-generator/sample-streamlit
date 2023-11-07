import streamlit as st
import json
import matplotlib.pyplot as plt

# Load data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Set a title and info section
st.title("My Streamlit Dashboard")
st.write("Welcome to my dashboard!")

# Pie Chart
st.subheader("Pie Chart")
pie_chart_data = data['pie_chart']
plt.pie(pie_chart_data['sizes'], labels=pie_chart_data['labels'])
st.pyplot( plt )

# Footer
st.write("Powered by Streamlit")
