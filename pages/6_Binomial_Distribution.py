import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

st.header('What is Binomial Distribution?')
st.write('The Binomial Distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.')
st.write('It is defined by two parameters: the number of trials \(n\) and the probability of success \(p\).')

def plot_binomial_distribution(n, p):
    """
    Plot the Binomial distribution curve for a specific number of trials (n) and probability (p) values.
    """
    x = np.arange(0, n + 1)
    bar_width = 0.25  # Width of each bar

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PMF
    pmf_y = binom.pmf(x, n, p)
    ax[0].bar(x, pmf_y, width=bar_width, color='blue', label=f'p={p}')
    ax[0].set_xlabel('Number of Successes')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title(f'Binomial Distribution PMF (n={n}, p={p})')
    ax[0].set_xticks(x)  # Set x-axis ticks to integers
    ax[0].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    # Plot CDF
    cdf_y = binom.cdf(x, n, p)
    ax[1].step(x, cdf_y, where='mid', color='blue', label=f'p={p}')
    ax[1].set_xlabel('Number of Successes')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title(f'Binomial Distribution CDF (n={n}, p={p})')
    ax[1].set_xticks(x)  # Set x-axis ticks to integers
    ax[1].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    st.pyplot(fig)

# Streamlit app
st.title('Interactive Binomial Distribution')

# Sliders for parameters
n_trials = st.slider("Number of Trials (n)", min_value=1, max_value=50, value=10)
p_success = st.slider("Probability of Success (p)", min_value=0.01, max_value=1.0, value=0.5, step=0.01)

plot_binomial_distribution(n_trials, p_success)

st.title('Binomial Distribution Formulas')

st.subheader('PMF of Binomial Distribution')
st.latex(r'''
    P(X=k|n, p) = 
    \binom{n}{k} p^k (1-p)^{n-k}
    ''')

st.subheader('CDF of Binomial Distribution')
st.latex(r'''
    F(x|n, p) = 
    \sum_{k=0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}
    ''')
