import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

st.header('What is Normal Distribution ?')
st.write('Normal Distribution is also known as Guassioan Disribution, It is most commonly used and is a continuous probability distribution that is symmetrical around the mean, with a bell shaped curve')
st.write("Two Parameters")
st.write("1) Mean - center of Distribution")
st.write("2) standard Deviation - Spread of Distribution")
st.write("Changing these two parameters, the mean and standard deviation, alters the distribution's shape as well")


def normal_distribution(mu, sigma, x):
    """
    Calculate the normal distribution (Gaussian) function.
    
    Parameters:
        mu (float): Mean of the distribution.
        sigma (float): Standard deviation of the distribution.
        x (numpy array): Values at which to evaluate the distribution.
    
    Returns:
        numpy array: Normal distribution values corresponding to the input x.
    """
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

def plot_pdf(mu1, sigma1, mu2, sigma2):
    """
    Plot the probability density function (PDF) for normal distributions.
    
    Parameters:
        mu1 (float): Mean of the first distribution.
        sigma1 (float): Standard deviation of the first distribution.
        mu2 (float): Mean of the second distribution.
        sigma2 (float): Standard deviation of the second distribution.
    """
    x = np.linspace(min(mu1 - 3*sigma1, mu2 - 3*sigma2), max(mu1 + 3*sigma1, mu2 + 3*sigma2), 1000)
    y1 = normal_distribution(mu1, sigma1, x)
    y2 = normal_distribution(mu2, sigma2, x)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].plot(x, y1, label='Fixed Distribution (PDF)', color='green')
    ax[0].plot(x, y2, label='Adjustable Distribution (PDF)', color='blue')

    # Add grid lines for mean
    ax[0].axvline(mu1, color='green', linestyle='--', label='Fixed Mean')
    ax[0].axvline(mu2, color='blue', linestyle='--', label='Adjustable Mean')
    
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper left')

    # Calculate and plot CDF
    cdf1 = norm.cdf(x, mu1, sigma1)
    cdf2 = norm.cdf(x, mu2, sigma2)
    ax[1].plot(x, cdf1, label='Fixed Distribution (CDF)', color='red', linestyle='-.')
    ax[1].plot(x, cdf2, label='Adjustable Distribution (CDF)', color='purple', linestyle='-.')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Streamlit app
st.title('Normal Distribution Curves')

# Fixed normal distribution parameters
fixed_mean = 0
fixed_std_dev = 1

# Adjustable normal distribution parameters
mean = st.slider('Mean (μ)', -10.0, 10.0, 0.0, 0.1, key='mean')
std_dev = st.slider('Standard Deviation (σ)', 0.1, 10.0, 1.0, 0.1, key='std_dev')

plot_pdf(fixed_mean, fixed_std_dev, mean, std_dev)



st.header('Normal Distribution PDF Formula')

st.latex(r'''
    f(x|\mu,\sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
    ''')

st.header('Normal Distribution CDF Formula')

st.latex(r'''
    F(x|\mu,\sigma^2) = \frac{1}{2} \left[1 + \text{erf}\left(\frac{x - \mu}{\sigma \sqrt{2}}\right)\right]
    ''')





