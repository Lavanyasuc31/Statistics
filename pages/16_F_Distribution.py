import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# Title
st.title('Exploring F-Distribution 📊')

# Introduction
st.header('What is F-Distribution?')
st.write("""
The **F-Distribution** is a continuous probability distribution that arises frequently in the analysis of variance (ANOVA). 
It is used primarily to compare two variances and has two degrees of freedom parameters:

### Key Parameters
1. **Degrees of Freedom 1 (d₁)**: Corresponds to the numerator degrees of freedom.
2. **Degrees of Freedom 2 (d₂)**: Corresponds to the denominator degrees of freedom.

The shape of the F-distribution changes based on the degrees of freedom.
""")

def plot_f_distribution(df1_1, df2_1, df1_2, df2_2):
    """
    Plot the F-distribution's PDF and CDF for given degrees of freedom.
    """
    x = np.linspace(0, 5, 1000)
    y1 = f.pdf(x, df1_1, df2_1)
    y2 = f.pdf(x, df1_2, df2_2)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # PDF Plot
    ax[0].plot(x, y1, label=f'F-Distribution (df₁={df1_1}, df₂={df2_1})', color='green')
    ax[0].plot(x, y2, label=f'F-Distribution (df₁={df1_2}, df₂={df2_2})', color='blue')
    ax[0].set_title('Probability Density Function (PDF)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend(loc='upper right')

    # CDF Plot
    cdf1 = f.cdf(x, df1_1, df2_1)
    cdf2 = f.cdf(x, df1_2, df2_2)
    ax[1].plot(x, cdf1, label=f'F-Distribution (df₁={df1_1}, df₂={df2_1})', color='red', linestyle='-.')
    ax[1].plot(x, cdf2, label=f'F-Distribution (df₁={df1_2}, df₂={df2_2})', color='purple', linestyle='-.')
    ax[1].set_title('Cumulative Distribution Function (CDF)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend(loc='lower right')

    st.pyplot(fig)

# Parameters for fixed distribution
fixed_df1 = 10
fixed_df2 = 20

# Widgets for adjustable distribution
st.sidebar.header('Adjustable F-Distribution Parameters')
df1 = st.sidebar.slider('Degrees of Freedom 1 (d₁)', 1, 30, 10)
df2 = st.sidebar.slider('Degrees of Freedom 2 (d₂)', 1, 30, 20)

# Plot distributions
plot_f_distribution(fixed_df1, fixed_df2, df1, df2)

# Mathematical Formulas
st.header('Formulas for F-Distribution')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|d_1,d_2) = \frac{\left(\frac{d_1}{d_2}\right)^{\frac{d_1}{2}} x^{\frac{d_1}{2}-1}}{\text{B}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)} \left(1 + \frac{d_1}{d_2}x\right)^{-\frac{d_1 + d_2}{2}}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|d_1,d_2) = I_{\frac{d_1 x}{d_1 x + d_2}} \left(\frac{d_1}{2}, \frac{d_2}{2}\right)
    ''')
