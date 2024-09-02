import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli

# Page title and introduction
st.title('Exploring Bernoulli Distribution 🎯')

st.header('What is Bernoulli Distribution?')
st.write("""
The **Bernoulli Distribution** is a discrete probability distribution for a random variable that can take one of two values: 
- **1** with probability \(p\) (representing success)
- **0** with probability \(1-p\) (representing failure).

This distribution models a single trial with two possible outcomes, making it a fundamental concept in probability theory. The Bernoulli distribution is also the building block for the **Binomial Distribution**, which represents the sum of multiple independent Bernoulli trials.
""")

# Function to plot Bernoulli Distribution
def plot_bernoulli_distribution(p):
    """
    Plot the Bernoulli distribution curves for a specific probability p.
    """
    x = np.array([0, 1])

    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PMF
    pmf_y = bernoulli.pmf(x, p)
    sns.barplot(x=x, y=pmf_y, ax=ax[0], palette='Blues_d', edgecolor='black')
    ax[0].set_xlabel('Outcome (x)')
    ax[0].set_ylabel('Probability Mass (PMF)')
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
st.header('Interactive Bernoulli Distribution')

# Slider for probability p
prob_success = st.slider("Probability of Success (p)", min_value=0.01, max_value=1.0, value=0.5, step=0.01)

# Plot the distribution based on user input
plot_bernoulli_distribution(prob_success)

# Mathematical Formulas Section
st.header('Bernoulli Distribution Formulas')

st.subheader('Probability Mass Function (PMF)')
st.latex(r'''
    P(X=x|p) = 
    \begin{cases} 
    p & x = 1 \\
    1 - p & x = 0
    \end{cases}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|p) = 
    \begin{cases} 
    0 & x < 0 \\
    1 - p & 0 \leq x < 1 \\
    1 & x \geq 1
    \end{cases}
    ''')

# Additional Information
st.header('Applications and Insights')
st.write("""
The Bernoulli Distribution is widely used in various fields, including:
- **Decision Making**: Modeling binary decisions (e.g., yes/no, pass/fail).
- **Economics**: Analyzing binary outcomes in market studies.
- **Clinical Trials**: Measuring the success/failure of treatments in a single trial.

Understanding this distribution is crucial for working with more complex distributions, such as the Binomial Distribution.
""")
