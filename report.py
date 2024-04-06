import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import _thread

# Initialize Firebase Admin
@st.cache(allow_output_mutation=True)
def init_firebase():
    if not firebase_admin._apps:
        # Use the service account information stored in Streamlit secrets
        cred = credentials.Certificate(st.secrets["FIREBASE"])
        firebase_admin.initialize_app(cred)
    return firestore.client()

# Function to fetch data from Firestore
def fetch_data(collection_name):
    db = init_firebase() # Ensure db is defined by calling init_firebase
    docs = db.collection(collection_name).get()
    return pd.DataFrame([doc.to_dict() for doc in docs]) # Proper indentation

# Streamlit UI setup
st.title('Firestore Data Viewer')

# Use the Firestore collection name from Streamlit secrets
collection_name = st.secrets["FIRESTORE_COLLECTION_NAME"]

if st.button('Fetch Data'):
    with st.spinner('Fetching data...'):
        data = fetch_data(collection_name)
        if not data.empty:
            st.write(data)
        else:
            st.warning('No data found in the collection.')
