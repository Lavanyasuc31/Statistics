import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import norm

# Title
st.title('Exploring Normal Distribution 📊')

# Introduction
st.header('What is Normal Distribution?')
st.write("""
The **Normal Distribution**, also known as the **Gaussian Distribution**, is a continuous probability distribution that is symmetrical around the mean. It is most commonly used in statistics and data analysis and has a characteristic bell-shaped curve.

### Key Parameters
1. **Mean (μ)**: This is the center of the distribution.
2. **Standard Deviation (σ)**: This measures the spread of the distribution.

Changing these parameters alters the shape of the distribution.
""")

def normal_distribution(mu, sigma, x):
    """
    Calculate the normal distribution (Gaussian) function.
    """
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

def plot_pdf_cdf(mu1, sigma1, mu2, sigma2):
    """
    Plot the probability density function (PDF) and cumulative distribution function (CDF) for normal distributions side by side with separate legends.
    """
    x = np.linspace(min(mu1 - 3*sigma1, mu2 - 3*sigma2), max(mu1 + 3*sigma1, mu2 + 3*sigma2), 1000)
    y1 = normal_distribution(mu1, sigma1, x)
    y2 = normal_distribution(mu2, sigma2, x)

    # Calculate CDF
    cdf1 = norm.cdf(x, mu1, sigma1)
    cdf2 = norm.cdf(x, mu2, sigma2)

    # Create subplots
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Probability Density Function (PDF)", "Cumulative Distribution Function (CDF)"),
        column_widths=[0.5, 0.5]
    )

    # Add PDF plot
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Fixed Distribution (PDF)', line=dict(color='green')), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Adjustable Distribution (PDF)', line=dict(color='blue')), row=1, col=1)
    fig.add_vline(x=mu1, line=dict(color='green', dash='dash'), row=1, col=1)
    fig.add_vline(x=mu2, line=dict(color='blue', dash='dash'), row=1, col=1)
    
    # Update PDF legend
    fig.update_layout(
        legend=dict(
            title="PDF Legend",
            x=0.1, y=0.2, traceorder="normal", orientation="v",
            font=dict(size=10, color="black")
        ),
        xaxis_title='x',
        yaxis_title='Probability Density',
    )

    # Add CDF plot
    fig.add_trace(go.Scatter(x=x, y=cdf1, mode='lines', name='Fixed Distribution (CDF)', line=dict(color='red', dash='dot')), row=1, col=2)
    fig.add_trace(go.Scatter(x=x, y=cdf2, mode='lines', name='Adjustable Distribution (CDF)', line=dict(color='purple', dash='dot')), row=1, col=2)

    # Update CDF legend
    fig.update_layout(
        legend=dict(
            title="CDF Legend",
            x=0.85, y=0.2, traceorder="normal", orientation="v",
            font=dict(size=10, color="black")
        ),
        xaxis2_title='x',
        yaxis2_title='Cumulative Probability',
    )

    fig.update_layout(
        title_text='Probability Density and Cumulative Distribution Functions',
        title_font=dict(color='black'),
        xaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),
        yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),
        xaxis2=dict(title_font=dict(color='black'), tickfont=dict(color='black')),
        yaxis2=dict(title_font=dict(color='black'), tickfont=dict(color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=50, r=50, t=50, b=50)
    )

    st.plotly_chart(fig)

# Parameters for fixed distribution
fixed_mean = 0
fixed_std_dev = 1

# Widgets for adjustable distribution
st.sidebar.header('Adjustable Distribution Parameters')
mean = st.sidebar.slider('Mean (μ)', -10.0, 10.0, 0.0, 0.1)
std_dev = st.sidebar.slider('Standard Deviation (σ)', 0.1, 10.0, 1.0, 0.1)

# Plot distributions
plot_pdf_cdf(fixed_mean, fixed_std_dev, mean, std_dev)


# Mathematical Formulas
st.header('Formulas for Normal Distribution')

st.subheader('Probability Density Function (PDF)')
st.latex(r'''
    f(x|\mu,\sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
    ''')

st.subheader('Cumulative Distribution Function (CDF)')
st.latex(r'''
    F(x|\mu,\sigma^2) = \frac{1}{2} \left[1 + \text{erf}\left(\frac{x - \mu}{\sigma \sqrt{2}}\right)\right]
    ''')
