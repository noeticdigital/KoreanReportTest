import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Function to generate random survey data
def generate_survey_data(num_responses=10):
    data = {
        "Age": np.random.randint(18, 65, size=num_responses),
        "Gender": np.random.choice(["Male", "Female", "Other"], size=num_responses),
        "Satisfaction": np.random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], size=num_responses),
        "Recommend": np.random.choice(["Yes", "No"], size=num_responses)
    }
    return pd.DataFrame(data)

# Function to create a random word cloud
def create_wordcloud():
    words = ['meeting', 'zoom', 'family', 'app', 'friend', 'good', 'business', 'people', 'services']
    word_freq = {word: np.random.randint(100, 1000) for word in words}
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freq)
    return wordcloud

# Main Streamlit app
st.title("Survey Data and Topics Visualization")

# Sidebar configuration
num_responses = st.sidebar.number_input("Number of Survey Responses", min_value=1, value=10, step=1)
app_mode = st.sidebar.selectbox("Select App Mode", ["Survey Data", "Topics and Sentiment"])

if app_mode == "Survey Data":
    # Generate and display survey data
    survey_data = generate_survey_data(num_responses)
    st.write("Survey Responses:")
    st.table(survey_data)
    
    # Data visualizations for survey data
    st.header("Data Visualizations")

    # Age Distribution
    fig, ax = plt.subplots()
    ax.hist(survey_data['Age'], bins='auto')
    ax.set_title("Age Distribution")
    st.pyplot(fig, use_container_width=True)

    # Additional visualizations can follow the same pattern

elif app_mode == "Topics and Sentiment":
    # Word Cloud Visualization
    wordcloud = create_wordcloud()
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig, use_container_width=True)

    # Additional topics and sentiment visualizations can be added here
