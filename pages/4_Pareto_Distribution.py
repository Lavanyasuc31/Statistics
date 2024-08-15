import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pareto

# Page title and introduction
st.title('Exploring Pareto Distribution 📊')

st.header('What is Pareto Distribution?')
st.write("""
The **Pareto Distribution** is a power-law distribution that is commonly used to model the distribution of wealth, income, and other quantities that exhibit a similar skewed behavior. Named after the Italian economist Vilfredo Pareto, it is often associated with the **80:20 rule**—where approximately 80% of the effects come from 20% of the causes.

### Key Characteristics:
- **Power Law**: There is a functional relationship between two quantities, where one quantity varies as a power of the other.
- **Right-Skewed**: Most values are clustered around the lower end, with a few very large values.
- **Heavy Tails**: The Pareto Distribution has a heavy tail, meaning extreme values are more probable compared to other distributions.
""")

# Function to plot Pareto Distribution
def plot_pareto_distribution(alpha):
    """
    Plot the Pareto distribution curves for a specific alpha value.
    """
    x = np.linspace(1, 5, 1000)  # Pareto distribution is defined for x >= 1
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PDFs
    y_pdf = pareto.pdf(x, alpha)
    sns.lineplot(x=x, y=y_pdf, ax=ax[0], color='blue', label=f'α={alpha}')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density (PDF)')
    ax[0].legend(loc='upper right')
    ax[0].set_title('Pareto Distribution PDF')
    ax[0].grid(True)

    # Plot CDFs
    y_cdf = pareto.cdf(x, alpha)
    sns.lineplot(x=x, y=y_cdf, ax=ax[1], color='orange', label=f'α={alpha}')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].legend(loc='lower right')
    ax[1].set_title('Pareto Distribution CDF')
    ax[1].grid(True)

    st.pyplot(fig)

# Sidebar for user input
st.sidebar.header('Pareto Distribution Parameters')
alpha = st.sidebar.slider("Shape Parameter (α)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

# Plot the distributions based on user input
st.header('Pareto Distribution Curves')
plot_pareto_distribution(alpha)

# Mathematical Formulas Section
st.header('Pareto Distribution Formulas')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|\alpha) = 
    \begin{cases} 
    \frac{\alpha}{x^{\alpha + 1}} & x \geq 1 \\
    0 & x < 1
    \end{cases}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\alpha) = 
    \begin{cases} 
    1 - \left(\frac{1}{x}\right)^\alpha & x \geq 1 \\
    0 & x < 1
    \end{cases}
    ''')

# Additional insights
st.header('Applications and Insights')
st.write("""
The Pareto Distribution is widely used in economics, sociology, and other fields to model phenomena with heavy-tailed distributions. Examples include:
- **Wealth Distribution**: A small percentage of the population controls a large portion of the wealth.
- **City Sizes**: A few cities have very large populations, while most are small.
- **File Sizes on the Internet**: A small number of very large files contribute to a significant portion of total traffic.

This distribution is useful when analyzing scenarios where extreme values are more frequent than in normal distributions.
""")
