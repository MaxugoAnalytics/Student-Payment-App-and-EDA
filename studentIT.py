import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
url = 'https://drive.google.com/uc?id=1QFcjwoJSZL5-hQ7iWN10WzQlxVHY59fW&export=download'
df = pd.read_csv(url)  # Use pandas to read the dataset from the URL

# Layout: Two rows and four columns for visuals
st.title("Dashboard - IT Survey Insights")

# Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Country Distribution")
    country_count = df['country'].value_counts()
    fig1 = plt.figure(figsize=(5, 4))
    sns.barplot(x=country_count.index, y=country_count.values)
    plt.xticks(rotation=45)
    plt.title('Country Distribution')
    st.pyplot(fig1)

with col2:
    st.subheader("Preferred IT Fields")
    it_field_count = df['preferred_IT_field'].value_counts()
    fig2 = plt.figure(figsize=(5, 4))
    sns.barplot(x=it_field_count.index, y=it_field_count.values)
    plt.xticks(rotation=45)
    plt.title('Preferred IT Fields')
    st.pyplot(fig2)

with col3:
    st.subheader("Final Payment Status")
    payment_status_count = df['final_payment_status'].value_counts()
    fig3 = plt.figure(figsize=(5, 4))
    sns.barplot(x=payment_status_count.index, y=payment_status_count.values)
    plt.xticks(rotation=45)
    plt.title('Payment Status')
    st.pyplot(fig3)

with col4:
    st.subheader("NDA Status")
    nda_status_count = df['nda_status'].value_counts()
    fig4 = plt.figure(figsize=(5, 4))
    sns.barplot(x=nda_status_count.index, y=nda_status_count.values)
    plt.xticks(rotation=45)
    plt.title('NDA Status')
    st.pyplot(fig4)

# Row 2
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.subheader("Likely to Pay")
    payment_likelihood = df['likely_to_paid'].value_counts()
    fig5 = plt.figure(figsize=(5, 4))
    sns.barplot(x=payment_likelihood.index, y=payment_likelihood.values)
    plt.xticks(rotation=45)
    plt.title('Likelihood to Pay')
    st.pyplot(fig5)

with col6:
    st.subheader("Region Distribution")
    region_count = df['region'].value_counts()
    fig6 = plt.figure(figsize=(5, 4))
    sns.barplot(x=region_count.index, y=region_count.values)
    plt.xticks(rotation=45)
    plt.title('Region Distribution')
    st.pyplot(fig6)

with col7:
    st.subheader("Survey Status")
    survey_status_count = df['nda_status'].value_counts()  # Assume NDA status is the survey status column
    fig7 = plt.figure(figsize=(5, 4))
    sns.barplot(x=survey_status_count.index, y=survey_status_count.values)
    plt.xticks(rotation=45)
    plt.title('Survey Status')
    st.pyplot(fig7)

with col8:
    st.subheader("Payment Status by Region")
    payment_region_df = df.groupby(['region', 'final_payment_status']).size().unstack().fillna(0)
    fig8 = payment_region_df.plot(kind='bar', stacked=True, figsize=(5, 4))
    plt.title('Payment Status by Region')
    st.pyplot(fig8)
