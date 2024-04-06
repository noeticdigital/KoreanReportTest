import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate random survey data
def generate_survey_data(num_responses=10):
    data = {
        "Age": np.random.randint(18, 65, size=num_responses),
        "Gender": np.random.choice(["Male", "Female", "Other"], size=num_responses),
        "Satisfaction": np.random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], size=num_responses),
        "Recommend": np.random.choice(["Yes", "No"], size=num_responses)
    }
    return pd.DataFrame(data)

st.title("Random Survey Data Display with Visualizations")

# Generating random survey data
num_responses = st.sidebar.number_input("Number of Responses", min_value=1, value=10, step=1)
survey_data = generate_survey_data(num_responses)

# Displaying the data in a table
st.write("Survey Responses:")
st.table(survey_data)

# Visualization
st.header("Data Visualizations")

# Age distribution with a histogram
st.subheader("Age Distribution")
age_values = survey_data["Age"]
st.bar_chart(age_values.value_counts().sort_index())

# Gender distribution with a bar chart
st.subheader("Gender Distribution")
gender_counts = survey_data["Gender"].value_counts()
st.bar_chart(gender_counts)

# Satisfaction levels with a bar chart
st.subheader("Satisfaction Levels")
satisfaction_counts = survey_data["Satisfaction"].value_counts()
st.bar_chart(satisfaction_counts)

# Recommendation ratio with a pie chart
st.subheader("Recommendation Ratio")
recommend_counts = survey_data["Recommend"].value_counts()
fig, ax = plt.subplots()
ax.pie(recommend_counts, labels=recommend_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
