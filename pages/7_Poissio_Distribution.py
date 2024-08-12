import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.header('What is Poisson Distribution?')
st.write('The Poisson Distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, given the average number of times the event occurs over that interval.')
st.write('It is commonly used for modeling the number of events occurring within a given time period, such as the number of emails received in an hour or the number of phone calls at a call center.')

def plot_poisson_distribution(lambda_):
    """
    Plot the Poisson distribution curve for a specific mean (λ) value.
    """
    max_x = 10  # Maximum x value to display (limiting to 10 events)
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    x = np.arange(0, max_x + 1)
    
    # Plot PMF
    pmf_y = poisson.pmf(x, lambda_)
    ax[0].bar(x, pmf_y, color='blue', width=0.4)
    ax[0].set_xlabel('Number of Events (x)')
    ax[0].set_ylabel('Probability Mass (PMF)')
    ax[0].set_title(f'Poisson Distribution PMF (λ={lambda_})')
    ax[0].set_xticks(x)
    ax[0].set_xticklabels([str(int(val)) for val in x])

    # Plot CDF
    cdf_y = poisson.cdf(x, lambda_)
    ax[1].step(x, cdf_y, where='mid', color='green')
    ax[1].set_xlabel('Number of Events (x)')
    ax[1].set_ylabel('Cumulative Distribution Function (CDF)')
    ax[1].set_title(f'Poisson Distribution CDF (λ={lambda_})')
    ax[1].set_xticks(x)
    ax[1].set_xticklabels([str(int(val)) for val in x])

    st.pyplot(fig)

# Streamlit app
st.title('Interactive Poisson Distribution')

# Slider for lambda value
lambda_value = st.slider("Select λ (Rate of Occurrence)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

plot_poisson_distribution(lambda_value)

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
