import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Set up the page title and introduction
st.title('Exploring Uniform Distribution 📊')

st.header('What is Uniform Distribution?')
st.write("""
The **Uniform Distribution** is a probability distribution where all outcomes are equally likely within a given range. It is characterized by:
1. **Lower Bound (a)**: The smallest value that can occur.
2. **Upper Bound (b)**: The largest value that can occur.

This distribution is often visualized as a rectangle where every value within the range [a, b] has the same probability.
""")

# Function to plot Uniform Distributions
def plot_uniform_distributions(a, b):
    x = np.linspace(a - 1, b + 1, 1000)
    pdf = uniform.pdf(x, a, b - a)
    cdf = uniform.cdf(x, a, b - a)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # PDF Plot
    sns.lineplot(x=x, y=pdf, ax=ax[0], color='purple', label='PDF')
    ax[0].axvline(a, color='purple', linestyle='--', label='Lower Bound (a)')
    ax[0].axvline(b, color='purple', linestyle='--', label='Upper Bound (b)')
    ax[0].set_title('Probability Density Function (PDF)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend(loc='upper left')

    # CDF Plot
    sns.lineplot(x=x, y=cdf, ax=ax[1], color='darkorange', label='CDF',linestyle='-.')
    ax[1].set_title('Cumulative Distribution Function (CDF)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Sidebar for uniform distribution parameters
st.sidebar.header('Uniform Distribution Parameters')
a = st.sidebar.slider('Lower Bound (a)', -10.0, 10.0, 0.0, 0.1)
b = st.sidebar.slider('Upper Bound (b)', -10.0, 10.0, 5.0, 0.1)

# Error handling and plot generation
if a >= b:
    st.error('Upper Bound (b) must be greater than Lower Bound (a).')
else:
    plot_uniform_distributions(a, b)

# Mathematical Formulas Section
st.header('Uniform Distribution Formulas')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|a,b) = 
    \begin{cases} 
    \frac{1}{b - a} & a \leq x \leq b \\
    0 & \text{otherwise}
    \end{cases}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|a,b) = 
    \begin{cases} 
    0 & x < a \\
    \frac{x - a}{b - a} & a \leq x \leq b \\
    1 & x > b
    \end{cases}
    ''')

# Additional Insights
st.header('Insights and Applications')
st.write("""
The Uniform Distribution is widely used in situations where each outcome within a range is equally likely, such as:
- Generating random numbers within a specific range.
- Modeling scenarios where outcomes within a specific range have equal probabilities, such as rolling a fair die.

It serves as a foundational concept in probability theory and is often used to model basic random processes.
""")
