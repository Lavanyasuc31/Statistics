import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson

# Page title and introduction
st.title('Exploring Poisson Distribution 📊')

st.header('What is Poisson Distribution?')
st.write("""
The **Poisson Distribution** is a discrete probability distribution that models the number of events occurring within a fixed interval of time or space, given a known average rate (λ) of occurrence. 
It is commonly used to predict the probability of a certain number of events happening in a specified time period, such as:
- The number of emails received in an hour.
- The number of phone calls at a call center.
- The number of accidents occurring at a busy intersection.

The Poisson Distribution assumes that events occur independently of one another.
""")

# Function to plot Poisson Distribution
def plot_poisson_distribution(lambda_):
    """
    Plot the Poisson distribution curve for a specific mean (λ) value.
    """
    max_x = 15  # Extend the range to show more possible events
    
    x = np.arange(0, max_x + 1)
    fig, ax = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Plot PMF
    pmf_y = poisson.pmf(x, lambda_)
    sns.barplot(x=x, y=pmf_y, ax=ax[0], palette='Blues_d', edgecolor='black')
    ax[0].set_xlabel('Number of Events (x)')
    ax[0].set_ylabel('Probability Mass Function (PMF)')
    ax[0].set_title(f'Poisson Distribution PMF (λ={lambda_})')
    ax[0].grid(True)

    # Plot CDF
    cdf_y = poisson.cdf(x, lambda_)
    sns.lineplot(x=x, y=cdf_y, ax=ax[1], color='green', marker='o')
    ax[1].set_xlabel('Number of Events (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].set_title(f'Poisson Distribution CDF (λ={lambda_})')
    ax[1].grid(True)

    st.pyplot(fig)

# Streamlit app
st.header('Interactive Poisson Distribution')

# Slider for lambda value
lambda_value = st.slider("Rate of Occurrence (λ)", min_value=0.1, max_value=15.0, value=1.0, step=0.1)

# Plot the distribution based on user input
plot_poisson_distribution(lambda_value)

# Mathematical Formulas Section
st.header('Poisson Distribution Formulas')

st.subheader('Probability Mass Function (PMF)')
st.latex(r'''
    P(X=k|\lambda) = 
    \frac{\lambda^k e^{-\lambda}}{k!}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\lambda) = 
    \sum_{k=0}^{\lfloor x \rfloor} \frac{\lambda^k e^{-\lambda}}{k!}
    ''')

# Additional Information Section
st.header('Applications and Insights')
st.write("""
The Poisson Distribution is useful in:
- **Queueing Theory**: Predicting the number of customers arriving at a service point.
- **Risk Management**: Modeling the occurrence of rare events such as natural disasters.
- **Operations Management**: Estimating the number of defects in a manufacturing process.

Understanding the Poisson Distribution helps in modeling real-world phenomena where the events are rare but have a measurable average rate.
""")
