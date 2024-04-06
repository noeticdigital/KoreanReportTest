import streamlit as st
import pandas as pd
import numpy as np

# Function to generate random survey data
def generate_survey_data(num_responses=10):
    # Assuming a survey with a few basic questions
    data = {
        "Age": np.random.randint(18, 65, size=num_responses),
        "Gender": np.random.choice(["Male", "Female", "Other"], size=num_responses),
        "Satisfaction": np.random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], size=num_responses),
        "Recommend": np.random.choice(["Yes", "No"], size=num_responses)
    }
    return pd.DataFrame(data)

st.title("Random Survey Data Display")

# Generating random survey data
num_responses = st.sidebar.number_input("Number of Responses", min_value=1, value=10, step=1)
survey_data = generate_survey_data(num_responses)

# Displaying the data in a table
st.write("Survey Responses:")
st.table(survey_data)
