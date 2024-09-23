import streamlit as st
from streamlit_extras.mention import mention
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

# Email sending function using SMTP
def send_email(name, feedback_type, feedback_message, rating):
    try:
        sender_email = "vijitsingh95@gmail.com"  # Replace with your email
        receiver_email = "vijitsingh95@gmail.com"  # Replace with your email
        password = "jqgl vbir egra neod"  # Replace with your email password or app-specific password

        # sender_email1 = "knisha987650@gmail.com"
        # receiver_email1 = "knisha987650@gmail.com"
        # password1 = "qzed esub spty maox"

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "New Feedback Received 🎉"

        # 2nd mail
        # msg1 = MIMEMultipart()
        # msg1['From'] = sender_email1
        # msg1['To'] = receiver_email1
        # msg1['Subject'] = "New Feedback Received 🎉"

        # Create the email body
        body = f"""
        You have received new feedback on your statistics notes:

        Name: {name}
        Feedback Type: {feedback_type}
        Feedback Message: {feedback_message}
        Rating: {rating}/5
        """

        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))

        # 2nd mail
        # msg1.attach(MIMEText(body, 'plain'))

        # Set up the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server1 = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # server1.starttls()
        server.login(sender_email, password)
        # server1.login(sender_email1, password1)
        text = msg.as_string()
        # text1 = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        # server1.sendmail(sender_email1, receiver_email1, text1)
        server.quit()
        # server1.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

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
        if send_email(name, feedback_type, feedback_message, rating):
            st.success("Thank you for your feedback! 🌟")
            st.balloons()
        else:
            st.error("Failed to send feedback. Please try again later.")

# Fun extra mentions or links
mention(label="Check out our other cool projects!", icon="💻", url="https://github.com/NiShAK-uMAri")
