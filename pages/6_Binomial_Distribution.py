import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

st.header('What is Binomial Distribution?')
st.write('The Binomial Distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.')
st.write('It is defined by two parameters: the number of trials \(n\) and the probability of success \(p\).')

def plot_binomial_distributions():
    """
    Plot the Binomial distribution curves for different probability and trial values.
    """
    n = 10
    ps = [0.2, 0.5, 0.8]
    colors = ['blue', 'green', 'red']
    labels = [r'$p=0.2$', r'$p=0.5$', r'$p=0.8$']
    bar_width = 0.25  # Width of each bar
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    x = np.arange(0, n+1)
    
    # Plot PMFs
    for i, (p, color, label) in enumerate(zip(ps, colors, labels)):
        y = binom.pmf(x, n, p)
        ax[0].bar(x + i * bar_width, y, width=bar_width, label=label, color=color)

    ax[0].set_xlabel('Number of Successes')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Binomial Distribution PMF')
    ax[0].set_xticks(x)  # Set x-axis ticks to integers
    ax[0].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    # Plot CDFs
    for i, (p, color, label) in enumerate(zip(ps, colors, labels)):
        y = binom.cdf(x, n, p)
        ax[1].step(x + i * bar_width, y, where='mid', label=label, color=color)

    ax[1].set_xlabel('Number of Successes')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Binomial Distribution CDF')
    ax[1].set_xticks(x)  # Set x-axis ticks to integers
    ax[1].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    st.pyplot(fig)

# Streamlit app
st.title('Binomial Distribution Curves')

plot_binomial_distributions()

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

