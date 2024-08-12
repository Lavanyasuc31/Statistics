import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

st.header('What is Pareto Distribution?')
st.write('The Pareto Distribution is used to model the distribution of wealth, income, and other quantities that exhibit a similar power-law behavior.')
st.write('Power Law is a functional relationship between two variables where one variable is proportional to the power of the other variable.')
st.write('The Pareto Distribution follows the 80:20 rule.')

def plot_pareto_distribution(alpha):
    """
    Plot the Pareto distribution curves for a specific alpha value.
    """
    x = np.linspace(1, 5, 1000)  # Pareto distribution is defined for x >= 1
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Plot PDFs
    y_pdf = pareto.pdf(x, alpha)
    ax[0].plot(x, y_pdf, label=f'α={alpha}', color='blue')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Pareto Distribution PDF')

    # Plot CDFs
    y_cdf = pareto.cdf(x, alpha)
    ax[1].plot(x, y_cdf, label=f'α={alpha}', color='blue')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Pareto Distribution CDF')

    st.pyplot(fig)

# Streamlit app
st.title('Interactive Pareto Distribution')

# Slider for alpha
alpha = st.slider("Shape Parameter (α)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

plot_pareto_distribution(alpha)

st.title('Pareto Distribution Formulas')

st.subheader('PDF of Pareto Distribution')
st.latex(r'''
    f(x|\alpha) = 
    \begin{cases} 
    \frac{\alpha}{x^{\alpha + 1}} & x \geq 1 \\
    0 & x < 1
    \end{cases}
    ''')

st.subheader('CDF of Pareto Distribution')
st.latex(r'''
    F(x|\alpha) = 
    \begin{cases} 
    1 - \left(\frac{1}{x}\right)^\alpha & x \geq 1 \\
    0 & x < 1
    \end{cases}
    ''')
