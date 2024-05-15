import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm,lognorm

st.header('What is Log-Normal Distribution ?')
st.write('Log-Normal Distribution is a Heavy Tailed continuous probability Distribution of a random variables whose logarithm is normally distributed.')
st.write("All right skewed distribution are not log-normal distribution.")
st.write("If X is log normally distributed then log(X) is normally distributed.")
st.write('Two parameters')
st.write("1) Mean - center of Distribution")
st.write("2) standard Deviation - Spread of Distribution")
st.write("Denoted as : X ~ log normal(mu,sigma)")
st.write("Changing these two parameters, the mean and standard deviation, alters the distribution's shape as well")


def plot_lognorm_distributions(mu, sigma):
    """
    Plot the probability density function (PDF) and cumulative distribution function (CDF)
    for a log-normal distribution.
    
    Parameters:
        mu (float): Mean of the underlying normal distribution.
        sigma (float): Standard deviation of the underlying normal distribution.
    """
    s = sigma
    scale = np.exp(mu)
    x_lognorm = np.linspace(lognorm.ppf(0.01, s, scale=scale), lognorm.ppf(0.99, s, scale=scale), 1000)
    
    pdf_lognorm = lognorm.pdf(x_lognorm, s, scale=scale)
    cdf_lognorm = lognorm.cdf(x_lognorm, s, scale=scale)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PDF
    ax[0].plot(x_lognorm, pdf_lognorm, label='Log-normal Distribution (PDF)', color='purple')

    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper right')

    # Plot CDF
    ax[1].plot(x_lognorm, cdf_lognorm, label='Log-normal Distribution (CDF)', color='purple', linestyle='-.')

    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Streamlit app
st.title('Log-normal Distribution Curves')

# Log-normal distribution parameters
st.header('Log-normal Distribution')
mu = st.slider('Mean of underlying normal distribution (μ)', -2.0, 2.0, 0.0, 0.1)
sigma = st.slider('Standard Deviation of underlying normal distribution (σ)', 0.1, 2.0, 0.5, 0.1)

plot_lognorm_distributions(mu, sigma)



st.title('Log-Normal Distribution Formulas')

st.subheader('PDF of Log-Normal Distribution')
st.latex(r'''
    f(x|\mu,\sigma) = 
    \begin{cases} 
    \frac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right) & x > 0 \\
    0 & x \leq 0
    \end{cases}
    ''')

st.subheader('CDF of Log-Normal Distribution')
st.latex(r'''
    F(x|\mu,\sigma) = 
    \begin{cases} 
    \frac{1}{2} \left[1 + \text{erf}\left(\frac{\ln x - \mu}{\sigma \sqrt{2}}\right)\right] & x > 0 \\
    0 & x \leq 0
    \end{cases}
    ''')