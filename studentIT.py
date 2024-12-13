import streamlit as st
import pandas as pd
import gdown

# Step 3: Download the data from Google Drive
url = 'https://drive.google.com/uc?id=1QFcjwoJSZL5-hQ7iWN10WzQlxVHY59fW&export=download'
output = 'survey_data.csv'

# Download the file
gdown.download(url, output, quiet=False)

# Load the data into a DataFrame
data = pd.read_csv(output)

# Step 4: Dashboard Setup
st.title("Survey Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by region
region_filter = st.sidebar.selectbox("Select Region", data["region"].unique())

# Filter by preferred IT field
field_filter = st.sidebar.selectbox("Select IT Field", data["preferred_IT_field"].unique())

# Filter by submission status
submission_status_filter = st.sidebar.selectbox("Select Submission Status", data["submission_status"].unique())

# Filter by survey status
survey_status_filter = st.sidebar.selectbox("Select Survey Status", data["survey_status"].unique())

# Step 5: Apply Filters to Data
filtered_data = data[
    (data["region"] == region_filter) &
    (data["preferred_IT_field"] == field_filter) &
    (data["submission_status"] == submission_status_filter) &
    (data["survey_status"] == survey_status_filter)
]

# Step 6: Display Data
st.subheader("Filtered Data")
st.write(filtered_data)

# Step 7: Data Visualizations
st.subheader("Data Visualizations")

# Display a bar chart for preferred IT field
st.bar_chart(filtered_data["preferred_IT_field"].value_counts())

# Display a bar chart for submission status
st.bar_chart(filtered_data["submission_status"].value_counts())

# Display a bar chart for survey status
st.bar_chart(filtered_data["survey_status"].value_counts())

# Step 8: Download the filtered data
st.subheader("Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_data.to_csv(index=False),
    file_name="filtered_survey_data.csv",
    mime="text/csv"
)

