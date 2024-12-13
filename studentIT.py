import streamlit as st
import pandas as pd

# Function to load the data
def load_data():
    url = "https://drive.google.com/uc?id=1OHLrMAwq8DDImDPDsLz_T2ASgdUT9TUn"
    data = pd.read_csv(url)
    return data

# Load the dataset
data = load_data()

# Page configuration
st.set_page_config(page_title="Applicant Dashboard", layout="wide")

# Title and Description
st.title("Applicant Management Dashboard")
st.markdown("""
This dashboard provides an overview of the applicant data, allowing filtering by multiple fields and summarizing key metrics.
""")

# Sidebar filters
st.sidebar.header("Filters")
country_filter = st.sidebar.multiselect("Select Country", options=data['country'].unique(), default=data['country'].unique())
region_filter = st.sidebar.multiselect("Select Region", options=data['region'].unique(), default=data['region'].unique())
team_filter = st.sidebar.multiselect("Select Team", options=data['ttl_team_assigned'].unique(), default=data['ttl_team_assigned'].unique())
field_filter = st.sidebar.multiselect("Select Preferred IT Field", options=data['preferred_IT_field'].unique(), default=data['preferred_IT_field'].unique())

# Apply filters
filtered_data = data[
    (data['country'].isin(country_filter)) &
    (data['region'].isin(region_filter)) &
    (data['ttl_team_assigned'].isin(team_filter)) &
    (data['preferred_IT_field'].isin(field_filter))
]

# Display data summary
st.subheader("Summary Metrics")
st.metric("Total Applicants", len(filtered_data))
st.metric("Unique Countries", filtered_data['country'].nunique())
st.metric("Unique IT Fields", filtered_data['preferred_IT_field'].nunique())

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Additional visualizations
st.subheader("Visualizations")
chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart"])

if chart_type == "Bar Chart":
    bar_data = filtered_data['country'].value_counts()
    st.bar_chart(bar_data)
elif chart_type == "Pie Chart":
    pie_data = filtered_data['preferred_IT_field'].value_counts()
    st.write(pie_data.plot.pie(autopct='%1.1f%%', startangle=90))
    st.pyplot()

# Footer
st.markdown("---")
st.caption("Data Source: Provided CSV file")
