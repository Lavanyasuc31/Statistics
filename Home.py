import streamlit as st
from PIL import Image
import base64
# from streamlit_extras.let_it_rain import rain

# Function to add a background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image
add_bg_from_local("./images/background.jpg")

# Main title with styling
st.markdown("<h1 style='text-align: center; color: white;'>📊 Welcome to Your Ultimate Guide to Statistics! 🎉</h1>", unsafe_allow_html=True)


# Display the main image with rounded corners
stats_image = Image.open("./images/banner_3_3.jpeg")  
st.image(stats_image, caption='Unleashing the Power of Data!', use_column_width=True)

# Introduction section with emojis and styled text
st.markdown("<h2 style='text-align: center; color: white;'>What You'll Discover Here 🕵️‍♂️</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; color: white;'>
Welcome to the world of Statistics, where numbers come alive and tell stories! 📚 Whether you're a newbie or a seasoned pro, 
this guide will take you on a journey through the magical land of data. From understanding how data distributes itself 🎯 
to testing your hypotheses like a true detective 🔍, we've got you covered!
</p>
""", unsafe_allow_html=True)

# Features of the guide with styled text and emojis
st.markdown("<h2 style='text-align: center; color: white;'>What's Inside? 📦</h2>", unsafe_allow_html=True)
st.markdown("""
<ul style='color: white;'>
<li><strong>Distributions Galore</strong> 🎲: Explore normal, binomial, Poisson, and more!</li>
<li><strong>Central Limit Theorem (CLT)</strong> 📈: Discover the law of large numbers in action.</li>
<li><strong>Hypothesis Testing</strong> 🧪: Put your theories to the test and uncover the truth!</li>
<li><strong>Confidence Intervals</strong> 🔎: Measure the uncertainty like a pro.</li>
<li><strong>And much more...</strong> 🚀</li>
</ul>
""", unsafe_allow_html=True)

# A fun closing note with styled text
st.markdown("<h2 style='text-align: center; color: white;'>Ready to Dive In? 🌊</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Let’s start crunching those numbers and uncovering the hidden stories in data. Dive into the notes, and may the odds (and p-values) be ever in your favor! 🎯</p>", unsafe_allow_html=True)

# Button to start learning
# if st.button("Start Learning 📚"):
#     st.write("Let's go! 🚀")

# if st.button("Start Learning 📚"):
#     rain(
#         emoji="📊📖",
#         font_size=54,
#         falling_speed=1,
#         animation_length=5,
#     )




st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


# Footer Section with Emojis
# Footer Section with Image Icons
# Adjusted Footer Section with Padding
# Footer Section with Image Icons
# Footer Section that Appears at the Bottom
st.markdown("""
    <style>
    .footer {
        width: 100%;
        text-align: center;
        color: white;
        padding: 10px 0;
        background-color: rgba(0, 0, 0, 0.5); /* Optional background for better visibility */
        margin-top: 50px; /* Adds some space above the footer */
    }
    </style>

    <div class="footer">
        <p>Created with ❤️ by Nisha 
            <a href='https://twitter.com' target='_blank'>
                <img src='https://img.icons8.com/fluent/48/000000/twitter.png' width='20' height='20'/>
            </a>
            | 
            <a href='https://linkedin.com' target='_blank'>
                <img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='20' height='20'/>
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

