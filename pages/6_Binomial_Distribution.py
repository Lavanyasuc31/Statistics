import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

# Page title and introduction
st.title('Exploring Binomial Distribution 🎲')

st.header('What is Binomial Distribution?')
st.write("""
The **Binomial Distribution** is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. 
It is defined by two parameters:
- **n**: the number of trials
- **p**: the probability of success in each trial.

The Binomial Distribution is used in various fields such as quality control, finance, and genetics, where the outcome of an experiment can be categorized as a success or failure.
""")

# Function to plot Binomial Distribution
def plot_binomial_distribution(n, p):
    """
    Plot the Binomial distribution curve for a specific number of trials (n) and probability (p) values.
    """
    x = np.arange(0, n + 1)
    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PMF
    pmf_y = binom.pmf(x, n, p)
    sns.barplot(x=x, y=pmf_y, ax=ax[0], palette='Blues_d', edgecolor='black')
    ax[0].set_xlabel('Number of Successes (k)')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].set_title(f'Binomial Distribution PMF (n={n}, p={p})')
    ax[0].set_xticks(x)  # Set x-axis ticks to integers
    ax[0].grid(True)

    # Plot CDF
    cdf_y = binom.cdf(x, n, p)
    sns.lineplot(x=x, y=cdf_y, ax=ax[1], color='blue', marker='o')
    ax[1].set_xlabel('Number of Successes (k)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].set_title(f'Binomial Distribution CDF (n={n}, p={p})')
    ax[1].set_xticks(x)  # Set x-axis ticks to integers
    ax[1].grid(True)

    st.pyplot(fig)

# Streamlit app
st.header('Interactive Binomial Distribution')

# Sliders for parameters
n_trials = st.slider("Number of Trials (n)", min_value=1, max_value=50, value=10)
p_success = st.slider("Probability of Success (p)", min_value=0.01, max_value=1.0, value=0.5, step=0.01)

# Plot the distribution based on user input
plot_binomial_distribution(n_trials, p_success)

# Mathematical Formulas Section
st.header('Binomial Distribution Formulas')

st.subheader('Probability Mass Function (PMF)')
st.latex(r'''
    P(X=k|n, p) = 
    \binom{n}{k} p^k (1-p)^{n-k}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|n, p) = 
    \sum_{k=0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}
    ''')

# Additional Information Section
st.header('Applications and Insights')
st.write("""
The Binomial Distribution is widely used in:
- **Quality Control**: Modeling the number of defective items in a batch.
- **Finance**: Analyzing the probability of achieving a certain number of successes in trading.
- **Medicine**: Studying the likelihood of treatment success in clinical trials.

Understanding the Binomial Distribution is crucial for solving real-world problems where outcomes are binary.
""")
