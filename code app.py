import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("medicine_details.csv")
    return df

df = load_data()

# Streamlit App UI
st.title("💊 Personalized Medicine Advisor")
st.write("Enter a medicine name to see usage, side effects, and substitutes.")

# User input
medicine_name = st.text_input("Medicine Name:")

if medicine_name:
    result = df[df['Drug_Name'].str.contains(medicine_name, case=False, na=False)]
    
    if result.empty:
        st.error("⚠️ No results found. Try another medicine.")
    else:
        st.success(f"Results for **{medicine_name}**:")
        st.dataframe(result[['Drug_Name', 'Uses', 'Side_effects', 'Substitute']])
