import random
import streamlit as st
from test_metrics import predict


# make the title of the page
st.title("Welcome to the Sentiment Analysis App")

# make the subheader of the page
st.subheader("Testing Demo Target for Prometheus")

# enter the text in the text area
st.text_area("Enter your text here", "Type something...")

# call the dummy predict button
btn = st.button("Analyze Sentiment")

if btn:
    random_delay = random.uniform(0.5, 2.0)  # Random delay between 0.5 and 2 seconds
    st.write(f"Simulating prediction with a delay of {random_delay:.2f}")
    
    # call the predict function
    sentiment_result = predict(random_delay)
    sentiment = sentiment_result["sentiment"]
    st.write(f"The sentiment of the text is: **{sentiment}**")