import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Survey Insights Dashboard", page_icon=":bar_chart:", layout="wide")
st.title(':bar_chart: Survey Insights Dashboard')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Load and cache data
@st.cache_data
def load_data():
    url = 'https://drive.google.com/uc?id=1QFcjwoJSZL5-hQ7iWN10WzQlxVHY59fW&export=download'
    df = pd.read_csv(url)
    return df

# Load data
df = load_data()

# Metrics Section
st.subheader("Key Metrics")
metrics_row = st.columns(5)
metrics_row[0].markdown(
    '<div class="metric-box">'
    '<div class="metric-title">Total Respondents</div>'
    f'<div class="metric-value">{df.shape[0]:,.0f}</div>'
    '</div>',
    unsafe_allow_html=True
)
metrics_row[1].markdown(
    '<div class="metric-box">'
    '<div class="metric-title">Unique Countries</div>'
    f'<div class="metric-value">{df["country"].nunique():,.0f}</div>'
    '</div>',
    unsafe_allow_html=True
)
metrics_row[2].markdown(
    '<div class="metric-box">'
    '<div class="metric-title">Preferred IT Fields</div>'
    f'<div class="metric-value">{df["preferred_IT_field"].nunique():,.0f}</div>'
    '</div>',
    unsafe_allow_html=True
)
metrics_row[3].markdown(
    '<div class="metric-box">'
    '<div class="metric-title">Payment Status</div>'
    f'<div class="metric-value">{df["final_payment_status"].nunique():,.0f}</div>'
    '</div>',
    unsafe_allow_html=True
)
metrics_row[4].markdown(
    '<div class="metric-box">'
    '<div class="metric-title">NDA Status</div>'
    f'<div class="metric-value">{df["nda_status"].nunique():,.0f}</div>'
    '</div>',
    unsafe_allow_html=True
)

# Data Visualizations Section
st.subheader("Data Visualizations")

# Row 1 (Four Columns)
row1 = st.columns(4)

with row1[0]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Country Distribution</div>', unsafe_allow_html=True)
    country_count = df['country'].value_counts()
    fig1 = px.bar(
        x=country_count.index,
        y=country_count.values,
        labels={'x': 'Country', 'y': 'Count'},
        title="Country Distribution"
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row1[1]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Preferred IT Fields</div>', unsafe_allow_html=True)
    it_field_count = df['preferred_IT_field'].value_counts()
    fig2 = px.bar(
        x=it_field_count.index,
        y=it_field_count.values,
        labels={'x': 'IT Field', 'y': 'Count'},
        title="Preferred IT Fields"
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row1[2]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Final Payment Status</div>', unsafe_allow_html=True)
    payment_status_count = df['final_payment_status'].value_counts()
    fig3 = px.bar(
        x=payment_status_count.index,
        y=payment_status_count.values,
        labels={'x': 'Payment Status', 'y': 'Count'},
        title="Payment Status"
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row1[3]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">NDA Status</div>', unsafe_allow_html=True)
    nda_status_count = df['nda_status'].value_counts()
    fig4 = px.bar(
        x=nda_status_count.index,
        y=nda_status_count.values,
        labels={'x': 'NDA Status', 'y': 'Count'},
        title="NDA Status"
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2 (Four Columns)
row2 = st.columns(4)

with row2[0]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Likely to Pay</div>', unsafe_allow_html=True)
    payment_likelihood = df['likely_to_paid'].value_counts()
    fig5 = px.bar(
        x=payment_likelihood.index,
        y=payment_likelihood.values,
        labels={'x': 'Likelihood to Pay', 'y': 'Count'},
        title="Likelihood to Pay"
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row2[1]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Region Distribution</div>', unsafe_allow_html=True)
    region_count = df['region'].value_counts()
    fig6 = px.bar(
        x=region_count.index,
        y=region_count.values,
        labels={'x': 'Region', 'y': 'Count'},
        title="Region Distribution"
    )
    st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row2[2]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Survey Status</div>', unsafe_allow_html=True)
    survey_status_count = df['nda_status'].value_counts()  # Assuming nda_status as survey status
    fig7 = px.bar(
        x=survey_status_count.index,
        y=survey_status_count.values,
        labels={'x': 'Survey Status', 'y': 'Count'},
        title="Survey Status"
    )
    st.plotly_chart(fig7, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with row2[3]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Payment Status by Region</div>', unsafe_allow_html=True)
    payment_region_df = df.groupby(['region', 'final_payment_status']).size().unstack().fillna(0)
    fig8 = px.bar(
        payment_region_df,
        labels={'final_payment_status': 'Payment Status', 'region': 'Region'},
        title="Payment Status by Region"
    )
    st.plotly_chart(fig8, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
