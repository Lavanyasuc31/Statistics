import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

st.header('What is Exponential Distribution?')
st.write('The Exponential Distribution is a continuous probability distribution that is often used to model the time between events in a Poisson process. It is defined by a single rate parameter, \( \lambda \), which is the rate of events per unit time.')
st.write('The Exponential Distribution is often used to model waiting times or lifetimes of objects.')

def plot_exponential_distributions():
    """
    Plot the Exponential distribution curves for different rate (λ) values.
    """
    lambdas = [0.5, 1, 2]
    colors = ['blue', 'green', 'red']
    labels = [r'$\lambda=0.5$', r'$\lambda=1$', r'$\lambda=2$']
    
    max_x = 10  # Maximum x value to display
    
    x = np.linspace(0, max_x, 1000)
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PDFs
    for lambda_, color, label in zip(lambdas, colors, labels):
        y = expon.pdf(x, scale=1/lambda_)
        ax[0].plot(x, y, label=label, color=color)

    ax[0].set_xlabel('Time (x)')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Exponential Distribution PDF')

    # Plot CDFs
    for lambda_, color, label in zip(lambdas, colors, labels):
        y = expon.cdf(x, scale=1/lambda_)
        ax[1].plot(x, y, label=label, color=color)

    ax[1].set_xlabel('Time (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Exponential Distribution CDF')

    st.pyplot(fig)

# Streamlit app
st.title('Exponential Distribution Curves')

plot_exponential_distributions()

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

