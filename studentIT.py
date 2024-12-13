import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IT Survey Insights", page_icon=":bar_chart:", layout="wide")
st.title(':bar_chart: IT Survey Insights Dashboard')

# Load and cache data
@st.cache_data
def load_data():
    url = 'https://drive.google.com/uc?id=1QFcjwoJSZL5-hQ7iWN10WzQlxVHY59fW&export=download'
    df = pd.read_csv(url)
    return df

# Load data
df = load_data()

# Key Metrics Section with Colored Boxes
st.subheader("Key Metrics")
metrics_row = st.columns(5)

# Key Metric 1: Total Revenue (Placeholder)
metrics_row[0].markdown(
    '''
    <div style="background-color:#00bfae;padding:20px;border-radius:10px;">
        <h3 style="color:white;">Total Revenue</h3>
        <h4 style="color:white;">${:,.2f}</h4>
    </div>
    '''.format(df["Order"].sum()), unsafe_allow_html=True
)

# Key Metric 2: Total Orders
metrics_row[1].markdown(
    '''
    <div style="background-color:#ff7043;padding:20px;border-radius:10px;">
        <h3 style="color:white;">Total Orders</h3>
        <h4 style="color:white;">{}</h4>
    </div>
    '''.format(df["Order"].sum()), unsafe_allow_html=True
)

# Key Metric 3: Unique Products
metrics_row[2].markdown(
    '''
    <div style="background-color:#ffeb3b;padding:20px;border-radius:10px;">
        <h3 style="color:black;">Unique Products</h3>
        <h4 style="color:black;">{}</h4>
    </div>
    '''.format(df["Style"].nunique()), unsafe_allow_html=True
)

# Key Metric 4: States Covered
metrics_row[3].markdown(
    '''
    <div style="background-color:#3f51b5;padding:20px;border-radius:10px;">
        <h3 style="color:white;">States Covered</h3>
        <h4 style="color:white;">{}</h4>
    </div>
    '''.format(df["ship-state"].nunique()), unsafe_allow_html=True
)

# Key Metric 5: Fulfillment Types
metrics_row[4].markdown(
    '''
    <div style="background-color:#8e24aa;padding:20px;border-radius:10px;">
        <h3 style="color:white;">Fulfillment Types</h3>
        <h4 style="color:white;">{}</h4>
    </div>
    '''.format(df["Fulfilment"].nunique()), unsafe_allow_html=True
)

# Data Visualizations Section
st.subheader("Data Visualizations")

# Row 1 (Four Columns)
row1 = st.columns(4)

with row1[0]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Country Distribution</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row1[1]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Preferred IT Fields</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row1[2]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Final Payment Status</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row1[3]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">NDA Status</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2 (Four Columns)
row2 = st.columns(4)

with row2[0]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Likelihood to Pay</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row2[1]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Region Distribution</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row2[2]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Survey Status</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)

with row2[3]:
    st.markdown('<div class="visual-box">', unsafe_allow_html=True)
    st.markdown('<div class="visual-title">Payment Status by Region</div>', unsafe_allow_html=True)
    # Visualization code here...
    st.markdown('</div>', unsafe_allow_html=True)
