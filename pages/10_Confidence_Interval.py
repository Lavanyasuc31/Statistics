import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy import stats

# Set the random seed for reproducibility
np.random.seed(42)

def compute_confidence_interval(sample, confidence=0.95, test_type='z'):
    """
    Compute the confidence interval for a sample using the z-test.
    """
    n = len(sample)
    mean = np.mean(sample)
    sem = stats.sem(sample)  # Standard error of the mean
    
    # Z-test uses normal distribution
    interval = sem * stats.norm.ppf((1 + confidence) / 2.)
    
    return mean, mean - interval, mean + interval, interval * 2  # Also return the interval width

def plot_candlestick_intervals(num_samples, sample_size, population_mean, population_std, confidence_level, x_axis_frequency):
    # Generate population
    population = np.random.normal(loc=population_mean, scale=population_std, size=10000)
    sample_means = []
    lower_bounds = []
    upper_bounds = []
    interval_widths = []
    includes_population_mean = []
    
    for _ in range(num_samples):
        sample = np.random.choice(population, sample_size)
        mean, lower_bound, upper_bound, interval_width = compute_confidence_interval(sample, confidence_level)
        sample_means.append(mean)
        lower_bounds.append(lower_bound)
        upper_bounds.append(upper_bound)
        interval_widths.append(interval_width)
        includes_population_mean.append(lower_bound <= population_mean <= upper_bound)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the population mean
    ax.axhline(y=population_mean, color='black', linestyle='--', label='Population Mean')
    ax.set_title(f'Candlestick Plot of Sample Means and {int(confidence_level*100)}% Confidence Intervals')
    ax.set_xlabel('Sample')
    ax.set_ylabel('Value')
    
    # Plot candlestick for each sample's mean and their confidence intervals
    for i in range(num_samples):
        color = 'green' if includes_population_mean[i] else 'red'
        ax.plot([i, i], [lower_bounds[i], upper_bounds[i]], color=color)  # Vertical line for CI
        ax.plot(i, sample_means[i], 'o', color=color)  # Sample mean

    # Adjust x-axis labels
    ax.set_xticks(range(0, num_samples, x_axis_frequency))
    ax.set_xticklabels(range(1, num_samples + 1, x_axis_frequency))
    ax.legend()
    st.pyplot(fig)

    # Display the interval data
    st.subheader("Confidence Intervals Details")
    interval_data = {
        "Sample": list(range(1, num_samples + 1)),
        "Sample Mean": sample_means,
        "Lower Bound": lower_bounds,
        "Upper Bound": upper_bounds,
        "Interval Width": interval_widths,
        "Includes Population Mean": includes_population_mean
    }
    st.dataframe(interval_data)

# Streamlit UI
st.title("Confidence Interval")
st.subheader("Confidence Interval")
st.write(""" - Confidence interval, in simple words, is a range of values within which we expect a particular 
population parameter, like a mean, to fall. It's a way to express the uncertainty around an estimate obtained from a sample of data. """)
st.subheader("Confidence Level")
st.write(""" - Confidence level, usually expressed as a percentage like 95%, indicates how sure we are that 
the true value lies within the interval. """)

st.write("**Confidence Interval = Point Estimate   +    Margin of Error** ")
st.write(""" - A point estimate is a single value, calculated from a sample, that serves as the best guess or approximation for an unknown population parameter, such as the mean or standard 
deviation. Point estimates are often used in statistics when we want to make inferences about a population based on a sample. """)
st.header("Confidence Intervals for Sample Means with 1000 Simulations")

# Input widgets for various parameters
sample_size = st.slider("Sample Size", min_value=1, max_value=500, value=30)
population_mean = st.number_input("Population Mean", value=0.0)
population_std = st.number_input("Population Standard Deviation", value=1.0, min_value=0.1)
num_samples = st.slider("Number of Simulations", min_value=1, max_value=1000, value=10)
confidence_level = st.slider("Confidence Level", min_value=0.80, max_value=0.99, value=0.95, step=0.01)
x_axis_frequency = st.slider("X-axis Label Frequency", min_value=1, max_value=num_samples, value=5)

# Generate and plot the graphs
plot_candlestick_intervals(num_samples, sample_size, population_mean, population_std, confidence_level, x_axis_frequency)
