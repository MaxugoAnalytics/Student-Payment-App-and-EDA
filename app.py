import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load preprocessed dataset
st.title("Nalytics Students Final Payment Status Prediction App")

# Load dataset and ensure columns retain integer types
@st.cache_data
def load_data():
    dtype_dict = {
        'country': 'int',
        'likely_to_paid': 'int',
        'expected_pay_usd': 'int',
        'id_submission_status': 'int',
        'survey_status': 'int',
        'signed_nda': 'int',
        'nda_status': 'int',
        'ttl_team_assigned': 'int',
        'id_status': 'int',
        'final_payment_status': 'int',
        'preferred_IT_field': 'int',
    }
    data = pd.read_csv(r"C:\Users\USER\Downloads\nalytics_data1.csv", dtype=dtype_dict)
    return data

# Call the function to load the dataset
data = load_data()

# Mapping dictionaries
country_mapping = {
    0: "Nigeria", 1: "South Africa", 2: "Kenya", 3: "Egypt", 4: "Ghana", 5: "Ethiopia",
    6: "Tanzania", 7: "Uganda", 8: "Algeria", 9: "Morocco", 10: "Angola", 11: "Sudan",
    12: "Senegal", 13: "Rwanda", 14: "Cameroon", 15: "Zimbabwe", 16: "Zambia", 17: "Mozambique",
    18: "Botswana", 19: "Malawi", 20: "Ivory Coast", 21: "Namibia", 22: "Burundi", 23: "Tunisia", 24: "Libya"}

likely_to_paid_map = {1: "True", 0: "False"}
id_submission_status_map = {1: "submitted", 0: "not_submitted"}
survey_status_map = {1: "accepted", 0: "rejected", 3: "pending"}
signed_nda_map = {1:'true', 2:'false', 3:'accepted'}
nda_status_map = {1: "accepted", 2: "rejected", 3: "info_requested", 4: "pending"}
ttl_team_assigned_map = {1:'uk_ai_team', 2:'fr_ai_team', 3:'us_ai_team', 4:'ch_ai_team'}
id_status_map = {1:'accepted', 2:'pending', 3:'false', 4:'rejected', 5:'info_requested'}
final_payment_status_map = {1: "Paid", 0: "Unpaid"}
preferred_IT_field_map = {
    'Cybersecurity': 0,
    'Artificial Intelligence': 1,
    'Software Development': 2,
    'Database Administration': 3,
    'Machine Learning': 4,
    'Web Development': 5,
    'Networking': 6,
    'Data Science': 7,
    'DevOps': 8,
    'Cloud Computing': 9}


# Display the dataset
st.subheader("Dataset Overview")
st.write("Here's a quick look at the dataset:")
st.dataframe(data.head())

# Visualize the final payment status distribution across countries
st.subheader("Payment Status Across Countries")
payment_by_country = data.groupby('country')['final_payment_status'].value_counts(normalize=True).unstack().fillna(0)
payment_by_country = payment_by_country.mul(100).round(1)  # Show percentage
fig, ax = plt.subplots(figsize=(10, 6))
payment_by_country.plot(kind='bar', stacked=True, ax=ax, color=['#FF5733', '#33FF57'])
ax.set_title('Percentage of Students Paid vs Unpaid by Country')
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Country')
ax.set_xticklabels([country_mapping[c] for c in payment_by_country.index], rotation=45, ha='right')
st.pyplot(fig)

# Visualize the correlation between expected pay and payment status
st.subheader("Correlation Between Expected Pay and Payment Status")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='final_payment_status', y='expected_pay_usd', data=data, ax=ax)
ax.set_title('Expected Pay vs Payment Status')
ax.set_xticklabels(['Unpaid', 'Paid'])
st.pyplot(fig)

# Prepare the data for model training
st.subheader("Model Training and Prediction")

# Define features (X) and target (y)
features = data.drop(columns=['final_payment_status'])
target = data['final_payment_status']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Build and Train the Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Convert accuracy to percentage
accuracy_percentage = accuracy * 100

# Display the accuracy as a percentage in the Streamlit app
st.write(f"Model Accuracy: **{accuracy_percentage:.2f}%**")

# User Input for Prediction
st.subheader("Make a Prediction")
# Dynamically create input fields based on feature columns
user_inputs = {}
for col in features.columns:
    if col == 'country':
        user_inputs[col] = st.selectbox(f"Select {col}", list(country_mapping.values()))
    elif col == 'likely_to_paid':
        user_inputs[col] = st.selectbox(f"Select {col}", list(likely_to_paid_map.values()))
    elif col == 'expected_pay_usd':
        user_inputs[col] = st.number_input(f"Enter {col}", value=data[col].median())
    elif col == 'id_submission_status':
        user_inputs[col] = st.selectbox(f"Select {col}", list(id_submission_status_map.values()))
    elif col == 'survey_status':
        user_inputs[col] = st.selectbox(f"Select {col}", list(survey_status_map.values()))
    elif col == 'signed_nda':
        user_inputs[col] = st.selectbox(f"Select {col}", list(signed_nda_map.values()))
    elif col == 'nda_status':
        user_inputs[col] = st.selectbox(f"Select {col}", list(nda_status_map.values()))
    elif col == 'ttl_team_assigned':
        user_inputs[col] = st.selectbox(f"Select {col}", list(ttl_team_assigned_map.values()))
    elif col == 'id_status':
        user_inputs[col] = st.selectbox(f"Select {col}", list(id_status_map.values()))
    elif col == 'preferred_IT_field':
        user_inputs[col] = st.selectbox(f"Select {col}", list(preferred_IT_field_map.keys()))

# Convert user inputs into a dataframe
input_data = pd.DataFrame([user_inputs])

# Map selected values back to numeric values for the model prediction
input_data['country'] = input_data['country'].map({v: k for k, v in country_mapping.items()})
input_data['likely_to_paid'] = input_data['likely_to_paid'].map({v: k for k, v in likely_to_paid_map.items()})
input_data['id_submission_status'] = input_data['id_submission_status'].map({v: k for k, v in id_submission_status_map.items()})
input_data['survey_status'] = input_data['survey_status'].map({v: k for k, v in survey_status_map.items()})
input_data['signed_nda'] = input_data['signed_nda'].map({v: k for k, v in signed_nda_map.items()})
input_data['nda_status'] = input_data['nda_status'].map({v: k for k, v in nda_status_map.items()})
input_data['ttl_team_assigned'] = input_data['ttl_team_assigned'].map({v: k for k, v in ttl_team_assigned_map.items()})
input_data['id_status'] = input_data['id_status'].map({v: k for k, v in id_status_map.items()})
input_data['preferred_IT_field'] = input_data['preferred_IT_field'].map({v: k for k, v in preferred_IT_field_map.items()})

# Make predictions using user inputs
if st.button("Predict"):
    prediction = model.predict(input_data)
    prediction_label = "Paid" if prediction[0] == 1 else "Not Paid"
    st.write(f"The predicted final payment status is: **{prediction_label}**")

# Display additional statistics to further engage users
st.subheader("Payment Status Insights")
total_paid = data[data['final_payment_status'] == 1].shape[0]
total_unpaid = data[data['final_payment_status'] == 0].shape[0]
st.write(f"**Total Paid Students**: {total_paid}")
st.write(f"**Total Unpaid Students**: {total_unpaid}")


