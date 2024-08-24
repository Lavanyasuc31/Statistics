import streamlit as st

# Page Title
st.title("Feedback Form")

# Introduction
st.write(
    """
    We value your feedback! Please fill out the form below to help us improve.
    """
)

# User Information
st.header("Personal Information")
name = st.text_input("Name:")
email = st.text_input("Email:")

# Feedback
st.header("Your Feedback")
rating = st.slider("How would you rate your experience?", 1, 5, 3)
suggestions = st.text_area("Any suggestions for improvement?")

# Submit Button
if st.button("Submit Feedback"):
    if name and email:
        st.success(f"Thank you for your feedback, {name}!")
        # Here, you could add code to save the feedback to a database or send it via email
    else:
        st.error("Please fill in all the required fields.")

# Optional: Display the feedback
st.header("Submitted Feedback")
st.write(f"Name: {name}")
st.write(f"Email: {email}")
st.write(f"Rating: {rating}")
st.write(f"Suggestions: {suggestions}")
