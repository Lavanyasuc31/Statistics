import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.header('What is Poisson Distribution?')
st.write('The Poisson Distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, given the average number of times the event occurs over that interval.')
st.write('It is commonly used for modeling the number of events occurring within a given time period, such as the number of emails received in an hour or the number of phone calls at a call center.')

def plot_poisson_distributions():
    """
    Plot the Poisson distribution curves for different mean (λ) values.
    """
    lambdas = [1, 4, 10]
    colors = ['blue', 'green', 'red']
    labels = [r'$\lambda=1$', r'$\lambda=4$', r'$\lambda=10$']
    
    max_x = 10  # Maximum x value to display (limiting to 10 events)
    bar_width = 0.25  # Width of each bar
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    x = np.arange(0, max_x + 1)
    
    # Plot PMFs
    for i, (lambda_, color, label) in enumerate(zip(lambdas, colors, labels)):
        y = poisson.pmf(x, lambda_)
        ax[0].bar(x + i * bar_width, y, width=bar_width, label=label, color=color)

    ax[0].set_xlabel('Number of Events (x)')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Poisson Distribution PMF')
    ax[0].set_xticks(x + bar_width)  # Adjust ticks to center them with bars
    ax[0].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    # Plot CDFs
    for i, (lambda_, color, label) in enumerate(zip(lambdas, colors, labels)):
        y = poisson.cdf(x, lambda_)
        ax[1].step(x + i * bar_width, y, where='mid', label=label, color=color)

    ax[1].set_xlabel('Number of Events (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Poisson Distribution CDF')
    ax[1].set_xticks(x)  # Keep ticks centered
    ax[1].set_xticklabels([str(int(val)) for val in x])  # Ensure labels are integers

    st.pyplot(fig)

# Streamlit app
st.title('Poisson Distribution Curves')

plot_poisson_distributions()

st.title('Poisson Distribution Formulas')

st.subheader('PMF of Poisson Distribution')
st.latex(r'''
    P(X=k|\lambda) = 
    \frac{\lambda^k e^{-\lambda}}{k!}
    ''')

st.subheader('CDF of Poisson Distribution')
st.latex(r'''
    F(x|\lambda) = 
    \sum_{k=0}^{\lfloor x \rfloor} \frac{\lambda^k e^{-\lambda}}{k!}
    ''')

