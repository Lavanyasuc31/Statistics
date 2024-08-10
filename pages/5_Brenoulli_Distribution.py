import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

st.header('What is Bernoulli Distribution?')
st.write('The Bernoulli Distribution is a discrete probability distribution for a random variable which takes the value 1 with probability \(p\) and the value 0 with probability \(1-p\).')
st.write('It models a single trial with two possible outcomes: success (1) and failure (0).')
st.write('The Bernoulli distribution is the building block for the Binomial distribution, which represents the sum of independent Bernoulli trials.')

def plot_bernoulli_distributions():
    """
    Plot the Bernoulli distribution curves for different probabilities p.
    """
    ps = [0.2, 0.5, 0.8]
    colors = ['blue', 'green', 'red']
    labels = [r'$p=0.2$', r'$p=0.5$', r'$p=0.8$']
    bar_width = 0.25  # Width of each bar
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    x = np.array([0, 1])
    
    # Plot PMFs
    for i, (p, color, label) in enumerate(zip(ps, colors, labels)):
        y = bernoulli.pmf(x, p)
        ax[0].bar(x + i * bar_width, y, width=bar_width, label=label, color=color)

    ax[0].set_xlabel('Outcome (x)')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Bernoulli Distribution PMF')
    ax[0].set_xticks(x + bar_width)  # Set the ticks in the middle of the bars
    ax[0].set_xticklabels(['0', '1'])  # Set the labels as 0 and 1

    # Plot CDFs
    for i, (p, color, label) in enumerate(zip(ps, colors, labels)):
        y = bernoulli.cdf(x, p)
        ax[1].step(x + i * bar_width, y, where='mid', label=label, color=color)

    ax[1].set_xlabel('Outcome (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Bernoulli Distribution CDF')
    ax[1].set_xticks(x + bar_width)  # Set the ticks in the middle of the steps
    ax[1].set_xticklabels(['0', '1'])  # Set the labels as 0 and 1

    st.pyplot(fig)

# Streamlit app
st.title('Bernoulli Distribution Curves')

plot_bernoulli_distributions()

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

