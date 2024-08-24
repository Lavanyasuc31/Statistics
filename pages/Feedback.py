import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.mention import mention

# Set a custom background image
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
    }
    .main-header {
        color: #ffffff;
        font-family: 'Comic Sans MS', sans-serif;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .fun-button {
        background-color: #ff6347;
        color: white;
        font-weight: bold;
        padding: 0.5em;
        border-radius: 10px;
        cursor: pointer;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>div>input {
        background-color: rgba(255, 255, 255, 0.8);
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add some rain effect for fun
# rain(emoji="✨", font_size=10, falling_speed=5, animation_length="infinite")

# Title with some flair
st.markdown("<h1 class='main-header'>We Value Your Feedback! 🎉</h1>", unsafe_allow_html=True)
st.write("Your feedback helps us to improve and create even more amazing experiences!")

# Feedback form
with st.form("feedback_form"):
    name = st.text_input("What's your name? 😊")
    feedback_type = st.selectbox("What kind of feedback do you have?", ["Praise 🙌", "Suggestion 💡", "Issue 🚨", "Other ✨"])
    feedback_message = st.text_area("Share your thoughts with us! 💬")
    rating = st.slider("How would you rate your experience?", 1, 5, 3)

    submitted = st.form_submit_button("Send Feedback")
    if submitted:
        st.success("Thank you for your feedback! 🌟")
        st.balloons()

# Fun extra mentions or links
mention(label="Check out our other cool projects!", icon="💻", url="https://github.com/NiShAK-uMAri")
