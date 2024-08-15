import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm

# Page title and introduction
st.title('Exploring Log-Normal Distribution 📊')

st.header('What is Log-Normal Distribution?')
st.write("""
The **Log-Normal Distribution** is a continuous probability distribution of a random variable whose logarithm is normally distributed. It is characterized by:
- **Right-skewness**: The distribution is skewed to the right, with a long tail on the positive side.
- **Heavy tails**: This distribution can model data with heavy tails, where extreme values are more likely.

### Key Points:
- If a random variable \(X\) follows a log-normal distribution, then \(\log(X)\) follows a normal distribution.
- The distribution is denoted as \(X \sim \text{Log-Normal}(\mu, \sigma)\), where \(\mu\) is the mean and \(\sigma\) is the standard deviation of the underlying normal distribution.

**Note:** Not all right-skewed distributions are log-normal.
""")

# Function to plot Log-Normal Distribution
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

    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PDF
    sns.lineplot(x=x_lognorm, y=pdf_lognorm, ax=ax[0], color='purple', label='PDF')
    ax[0].set_title('Probability Density Function (PDF)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend(loc='upper right')
    ax[0].grid(True)

    # Plot CDF
    sns.lineplot(x=x_lognorm, y=cdf_lognorm, ax=ax[1], color='orange', label='CDF', linestyle='-.')
    ax[1].set_title('Cumulative Distribution Function (CDF)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend(loc='lower right')
    ax[1].grid(True)

    st.pyplot(fig)

# Sidebar for user input
st.sidebar.header('Log-Normal Distribution Parameters')
mu = st.sidebar.slider('Mean of underlying normal distribution (μ)', -2.0, 2.0, 0.0, 0.1)
sigma = st.sidebar.slider('Standard Deviation of underlying normal distribution (σ)', 0.1, 2.0, 0.5, 0.1)

# Plot the distributions based on user input
st.header('Log-Normal Distribution Curves')
plot_lognorm_distributions(mu, sigma)

# Mathematical Formulas Section
st.header('Log-Normal Distribution Formulas')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|\mu,\sigma) = 
    \begin{cases} 
    \frac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right) & x > 0 \\
    0 & x \leq 0
    \end{cases}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\mu,\sigma) = 
    \begin{cases} 
    \frac{1}{2} \left[1 + \text{erf}\left(\frac{\ln x - \mu}{\sigma \sqrt{2}}\right)\right] & x > 0 \\
    0 & x \leq 0
    \end{cases}
    ''')

# Additional insights
st.header('Insights and Applications')
st.write("""
The Log-Normal Distribution is commonly used in various fields to model positive-valued data that exhibit a right-skewed distribution. Some applications include:
- Modeling stock prices and financial returns, as prices cannot be negative and are often skewed.
- Representing the distribution of income, where a small number of individuals earn much higher than the average.
- Describing the size distribution of biological organisms, where larger sizes are less common.

This distribution is versatile and applicable in any situation where the data is positive and skewed to the right.
""")
