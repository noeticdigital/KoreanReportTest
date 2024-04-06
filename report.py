import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns

# Random data for word cloud
def create_wordcloud():
    words = ['meeting', 'zoom', 'family', 'app', 'friend', 'good', 'business', 'people', 'services']
    word_freq = {word: np.random.randint(100, 1000) for word in words}
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freq)
    return wordcloud

# Random data for bar chart
def create_bar_chart():
    categories = ['technical', 'billing', 'support', 'bugs', 'urgent', 'performance']
    values = np.random.randint(100, 5000, size=len(categories))
    df = pd.DataFrame({'categories': categories, 'values': values})
    return df

# Random data for line chart
def create_line_chart_data():
    categories = ['technical', 'billing', 'support', 'bugs', 'urgent', 'performance']
    df = pd.DataFrame({'Date': pd.date_range(start='1/1/2024', periods=100)})
    for category in categories:
        df[category] = np.random.randint(100, 1000, size=len(df))
    return df

# Streamlit app layout
st.title('Topics and Sentiment')

# Word Cloud
wordcloud = create_wordcloud()
fig, ax = plt.subplots(figsize=(8, 4))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Bar Chart
df_bar = create_bar_chart()
fig, ax = plt.subplots()
sns.barplot(x='categories', y='values', data=df_bar, ax=ax)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Line Chart
df_line = create_line_chart_data()
fig, ax = plt.subplots()
for category in df_line.columns[1:]:
    ax.plot(df_line['Date'], df_line[category], label=category)
plt.legend(loc='upper left')
st.pyplot(fig)

# Placeholder for PDF download button (to be implemented)
st.markdown('Download PDF --')
