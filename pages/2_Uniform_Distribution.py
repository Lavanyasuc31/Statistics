import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform

st.header('What is Uniform Distribution ?')
st.write('Uniform Distribution is a probability DIstribution where all the outcomes are equally likely within a given range')
st.write("Two Parameters")
st.write("1) a - Lower Value")
st.write("2) b - Higher Value")


def plot_uniform_distributions(a, b):
    """
    Plot the probability density function (PDF) and cumulative distribution function (CDF)
    for a uniform distribution.
    
    Parameters:
        a (float): Lower bound of the uniform distribution.
        b (float): Upper bound of the uniform distribution.
    """
    x_unif = np.linspace(a - 1, b + 1, 1000)
    
    y_unif = uniform.pdf(x_unif, a, b - a)
    cdf_unif = uniform.cdf(x_unif, a, b - a)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PDF
    ax[0].plot(x_unif, y_unif, label='Uniform Distribution (PDF)', color='purple')

    ax[0].axvline(a, color='purple', linestyle='--', label='a')
    ax[0].axvline(b, color='purple', linestyle='--', label='b')

    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper left')

    # Plot CDF
    ax[1].plot(x_unif, cdf_unif, label='Uniform Distribution (CDF)', color='purple', linestyle='-.')

    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Streamlit app
st.title('Uniform Distribution Curves')

# Uniform distribution parameters
st.header('Uniform Distribution')
a = st.slider('Lower Bound (a)', -10.0, 10.0, 0.0, 0.1)
b = st.slider('Upper Bound (b)', -10.0, 10.0, 5.0, 0.1)

if a >= b:
    st.error('Upper Bound (b) must be greater than Lower Bound (a).')
else:
    plot_uniform_distributions(a, b)


st.title('Uniform Distribution Formulas')

st.subheader('PDF of Uniform Distribution')
st.latex(r'''
    f(x|a,b) = 
    \begin{cases} 
    \frac{1}{b - a} & a \leq x \leq b \\
    0 & \text{otherwise}
    \end{cases}
    ''')

st.subheader('CDF of Uniform Distribution')
st.latex(r'''
    F(x|a,b) = 
    \begin{cases} 
    0 & x < a \\
    \frac{x - a}{b - a} & a \leq x \leq b \\
    1 & x > b
    \end{cases}
    ''')