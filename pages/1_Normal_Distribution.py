import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Title
st.title('Exploring Normal Distribution 📊')

# Introduction
st.header('What is Normal Distribution?')
st.write("""
The **Normal Distribution**, also known as the **Gaussian Distribution**, is a continuous probability distribution that is symmetrical around the mean. It is most commonly used in statistics and data analysis and has a characteristic bell-shaped curve.

### Key Parameters
1. **Mean (μ)**: This is the center of the distribution.
2. **Standard Deviation (σ)**: This measures the spread of the distribution.

Changing these parameters alters the shape of the distribution.
""")

def normal_distribution(mu, sigma, x):
    """
    Calculate the normal distribution (Gaussian) function.
    """
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

def plot_pdf(mu1, sigma1, mu2, sigma2):
    """
    Plot the probability density function (PDF) and cumulative distribution function (CDF) for normal distributions.
    """
    x = np.linspace(min(mu1 - 3*sigma1, mu2 - 3*sigma2), max(mu1 + 3*sigma1, mu2 + 3*sigma2), 1000)
    y1 = normal_distribution(mu1, sigma1, x)
    y2 = normal_distribution(mu2, sigma2, x)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # PDF Plot
    ax[0].plot(x, y1, label='Fixed Distribution (PDF)', color='green')
    ax[0].plot(x, y2, label='Adjustable Distribution (PDF)', color='blue')
    ax[0].axvline(mu1, color='green', linestyle='--', label='Fixed Mean')
    ax[0].axvline(mu2, color='blue', linestyle='--', label='Adjustable Mean')
    ax[0].set_title('Probability Density Function (PDF)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend(loc='upper left')

    # CDF Plot
    cdf1 = norm.cdf(x, mu1, sigma1)
    cdf2 = norm.cdf(x, mu2, sigma2)
    ax[1].plot(x, cdf1, label='Fixed Distribution (CDF)', color='red', linestyle='-.')
    ax[1].plot(x, cdf2, label='Adjustable Distribution (CDF)', color='purple', linestyle='-.')
    ax[1].set_title('Cumulative Distribution Function (CDF)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Parameters for fixed distribution
fixed_mean = 0
fixed_std_dev = 1

# Widgets for adjustable distribution
st.sidebar.header('Adjustable Distribution Parameters')
mean = st.sidebar.slider('Mean (μ)', -10.0, 10.0, 0.0, 0.1)
std_dev = st.sidebar.slider('Standard Deviation (σ)', 0.1, 10.0, 1.0, 0.1)

# Plot distributions
plot_pdf(fixed_mean, fixed_std_dev, mean, std_dev)

# Mathematical Formulas
st.header('Formulas for Normal Distribution')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|\mu,\sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\mu,\sigma^2) = \frac{1}{2} \left[1 + \text{erf}\left(\frac{x - \mu}{\sigma \sqrt{2}}\right)\right]
    ''')
