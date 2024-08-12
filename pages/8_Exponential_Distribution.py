import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

st.header('What is Exponential Distribution?')
st.write('The Exponential Distribution is a continuous probability distribution that is often used to model the time between events in a Poisson process. It is defined by a single rate parameter, \( \lambda \), which is the rate of events per unit time.')
st.write('The Exponential Distribution is often used to model waiting times or lifetimes of objects.')

def plot_exponential_distribution(lambda_):
    """
    Plot the Exponential distribution curve for a specific rate (λ) value.
    """
    max_x = 10  # Maximum x value to display
    x = np.linspace(0, max_x, 1000)
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

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
st.title('Interactive Exponential Distribution')

# Slider for lambda value
lambda_value = st.slider("Select λ (Rate of Events)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

plot_exponential_distribution(lambda_value)

st.title('Exponential Distribution Formulas')

st.subheader('PDF of Exponential Distribution')
st.latex(r'''
    f(x|\lambda) = 
    \begin{cases} 
    \lambda e^{-\lambda x} & x \geq 0 \\
    0 & x < 0
    \end{cases}
    ''')

st.subheader('CDF of Exponential Distribution')
st.latex(r'''
    F(x|\lambda) = 
    \begin{cases} 
    1 - e^{-\lambda x} & x \geq 0 \\
    0 & x < 0
    \end{cases}
    ''')
