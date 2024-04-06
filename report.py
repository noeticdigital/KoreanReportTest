import streamlit as st
import pandas as pd
import numpy as np

# Attempt to import matplotlib, handling the potential import error gracefully
try:
    import matplotlib.pyplot as plt
    matplotlib_installed = True
except ImportError:
    matplotlib_installed = False
    st.error("Error importing matplotlib. Please ensure it is installed.")

def generate_survey_data(num_responses=10):
    data = {
        "Age": np.random.randint(18, 65, size=num_responses),
        "Gender": np.random.choice(["Male", "Female", "Other"], size=num_responses),
        "Satisfaction": np.random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], size=num_responses),
        "Recommend": np.random.choice(["Yes", "No"], size=num_responses)
    }
    return pd.DataFrame(data)

st.title("Random Survey Data Display with Visualizations")

# Sidebar configuration
num_responses = st.sidebar.number_input("Number of Responses", min_value=1, value=10, step=1)

# Generate and display survey data
survey_data = generate_survey_data(num_responses)
st.write("Survey Responses:")
st.table(survey_data)

# Data visualization section
if matplotlib_installed:  # Only proceed with visualizations if matplotlib is available
    st.header("Data Visualizations")

    # Age distribution with a histogram
    st.subheader("Age Distribution")
    st.bar_chart(survey_data["Age"].value_counts().sort_index())

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
    if len(survey_data["Recommend"].unique()) > 1:  # Check if there's more than one unique response for Recommendations
        recommend_counts = survey_data["Recommend"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(recommend_counts, labels=recommend_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
    else:
        st.write("Not enough variety in responses to generate a recommendation ratio pie chart.")
