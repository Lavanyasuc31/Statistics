import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pareto

st.header('What is Pareto Distribution ?')
st.write('Pareto Distribution is used to model the distribution of wealth, income and other quantities that exhibit a similar power-law behaviour.')
st.write('What is power Law?')
st.write('Power Law is a functional relationship between two variables where one variable is proportional to the power of the other variable.')
st.write('Pareto Distribution follows 80:20 rule')


def pareto_distribution(alpha, x):
    """
    Calculate the Pareto distribution (PDF) function.
    
    Parameters:
        alpha (float): Shape parameter of the distribution.
        x (numpy array): Values at which to evaluate the distribution.
    
    Returns:
        numpy array: Pareto distribution values corresponding to the input x.
    """
    return pareto.pdf(x, alpha)

def plot_pareto_distributions():
    """
    Plot the Pareto distribution curves for different alpha values.
    """
    x = np.linspace(1, 5, 1000)  # Pareto distribution is defined for x >= 1
    
    alphas = [1, 2, 3, np.inf]
    colors = ['purple', 'blue', 'green', 'red']
    labels = [r'$\alpha=1$', r'$\alpha=2$', r'$\alpha=3$', r'$\alpha=\infty$']
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PDFs
    for alpha, color, label in zip(alphas, colors, labels):
        if alpha == np.inf:
            y = np.zeros_like(x)
            y[x == 1] = np.inf  # Delta function at x = 1
        else:
            y = pareto.pdf(x, alpha)
        ax[0].plot(x, y, label=label, color=color)

    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Pareto Distribution PDF')

    # Plot CDFs
    for alpha, color, label in zip(alphas, colors, labels):
        if alpha == np.inf:
            y = np.heaviside(x - 1, 1)  # Heaviside step function
        else:
            y = pareto.cdf(x, alpha)
        ax[1].plot(x, y, label=label, color=color)

    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Pareto Distribution CDF')

    st.pyplot(fig)

# Streamlit app
st.title('Pareto Distribution Curves')

plot_pareto_distributions()


st.title('Pareto Distribution Formulas')

st.subheader('PDF of Pareto Distribution')
st.latex(r'''
    f(x|x_m, \alpha) = 
    \begin{cases} 
    \frac{\alpha x_m^\alpha}{x^{\alpha + 1}} & x \geq x_m \\
    0 & x < x_m
    \end{cases}
    ''')

st.subheader('CDF of Pareto Distribution')
st.latex(r'''
    F(x|x_m, \alpha) = 
    \begin{cases} 
    1 - \left(\frac{x_m}{x}\right)^\alpha & x \geq x_m \\
    0 & x < x_m
    \end{cases}
    ''')