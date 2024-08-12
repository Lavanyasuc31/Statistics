import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

st.header('What is Bernoulli Distribution?')
st.write('The Bernoulli Distribution is a discrete probability distribution for a random variable which takes the value 1 with probability \(p\) and the value 0 with probability \(1-p\).')
st.write('It models a single trial with two possible outcomes: success (1) and failure (0).')
st.write('The Bernoulli distribution is the building block for the Binomial distribution, which represents the sum of independent Bernoulli trials.')

def plot_bernoulli_distribution(p):
    """
    Plot the Bernoulli distribution curves for a specific probability p.
    """
    x = np.array([0, 1])
    bar_width = 0.25  # Width of each bar

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PMF
    pmf_y = bernoulli.pmf(x, p)
    ax[0].bar(x, pmf_y, width=bar_width, color='blue', label=f'p={p}')
    ax[0].set_xlabel('Outcome (x)')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title(f'Bernoulli Distribution PMF (p={p})')
    ax[0].set_xticks(x)  # Set x-axis ticks to integers
    ax[0].set_xticklabels(['0', '1'])  # Ensure labels are 0 and 1

    # Plot CDF
    cdf_y = bernoulli.cdf(x, p)
    ax[1].step(x, cdf_y, where='mid', color='blue', label=f'p={p}')
    ax[1].set_xlabel('Outcome (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title(f'Bernoulli Distribution CDF (p={p})')
    ax[1].set_xticks(x)  # Set x-axis ticks to integers
    ax[1].set_xticklabels(['0', '1'])  # Ensure labels are 0 and 1

    st.pyplot(fig)

# Streamlit app
st.title('Interactive Bernoulli Distribution')

# Slider for probability p
prob_success = st.slider("Probability of Success (p)", min_value=0.01, max_value=1.0, value=0.5, step=0.01)

plot_bernoulli_distribution(prob_success)

st.title('Bernoulli Distribution Formulas')

st.subheader('PMF of Bernoulli Distribution')
st.latex(r'''
    P(X=x|p) = 
    \begin{cases} 
    p & x = 1 \\
    1 - p & x = 0
    \end{cases}
    ''')

st.subheader('CDF of Bernoulli Distribution')
st.latex(r'''
    F(x|p) = 
    \begin{cases} 
    0 & x < 0 \\
    1 - p & 0 \leq x < 1 \\
    1 & x \geq 1
    \end{cases}
    ''')
