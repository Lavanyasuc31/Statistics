import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon

# Page title and introduction
st.title('Exploring Exponential Distribution ⏳')

st.header('What is Exponential Distribution?')
st.write("""
The **Exponential Distribution** is a continuous probability distribution used to model the time between events in a Poisson process. 
It is characterized by a single rate parameter \( \lambda \), representing the average number of events per unit time. This distribution is widely used in fields such as:
- **Queueing Theory**: Modeling waiting times in queues.
- **Reliability Engineering**: Estimating the lifespan of products or systems.
- **Telecommunications**: Predicting time intervals between successive phone calls.

The Exponential Distribution is memoryless, meaning the probability of an event occurring in the future is independent of how much time has already elapsed.
""")

# Function to plot Exponential Distribution
def plot_exponential_distribution(lambda_):
    """
    Plot the Exponential distribution curve for a specific rate (λ) value.
    """
    max_x = 10  # Maximum x value to display
    x = np.linspace(0, max_x, 1000)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PDF
    pdf_y = expon.pdf(x, scale=1/lambda_)
    ax[0].plot(x, pdf_y, label=f'λ={lambda_}', color='blue')
    ax[0].set_xlabel('Time (x)')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].set_title(f'Exponential Distribution PDF (λ={lambda_})')

    # Plot CDF
    cdf_y = expon.cdf(x, scale=1/lambda_)
    ax[1].plot(x, cdf_y, label=f'λ={lambda_}', color='green')
    ax[1].set_xlabel('Time (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].set_title(f'Exponential Distribution CDF (λ={lambda_})')

    st.pyplot(fig)

# Streamlit app
st.header('Interactive Exponential Distribution')

# Slider for lambda value
lambda_value = st.slider("Select λ (Rate of Events)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

# Plot the distribution based on user input
plot_exponential_distribution(lambda_value)

# Mathematical Formulas Section
st.header('Exponential Distribution Formulas')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|\lambda) = 
    \begin{cases} 
    \lambda e^{-\lambda x} & x \geq 0 \\
    0 & x < 0
    \end{cases}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\lambda) = 
    \begin{cases} 
    1 - e^{-\lambda x} & x \geq 0 \\
    0 & x < 0
    \end{cases}
    ''')

# Additional Information Section
st.header('Key Properties and Applications')
st.write("""
The Exponential Distribution is particularly useful in scenarios where the events are memoryless, meaning the future probability is independent of the past.
- **Memoryless Property**: The probability that an event occurs in the next time unit is the same, regardless of how much time has already passed.
- **Mean and Variance**: The mean and standard deviation of the Exponential Distribution are both equal to \( \frac{1}{\lambda} \), giving a clear relationship between the rate parameter and the distribution's spread.

Understanding the Exponential Distribution helps in modeling various real-world processes, particularly in reliability engineering and queueing systems.
""")
