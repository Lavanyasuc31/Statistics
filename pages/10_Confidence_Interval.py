import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy import stats

# Set the random seed for reproducibility
np.random.seed(42)

def compute_confidence_interval(sample, confidence=0.95):
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
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot the population mean
    ax.axhline(y=population_mean, color='black', linestyle='--', label='Population Mean')
    ax.set_title(f'Candlestick Plot of Sample Means and {int(confidence_level*100)}% Confidence Intervals', fontsize=16)
    ax.set_xlabel('Sample Index', fontsize=14)
    ax.set_ylabel('Value', fontsize=14)
    
    # Plot candlestick for each sample's mean and their confidence intervals
    for i in range(num_samples):
        color = 'green' if includes_population_mean[i] else 'red'
        ax.plot([i, i], [lower_bounds[i], upper_bounds[i]], color=color)  # Vertical line for CI
        ax.plot(i, sample_means[i], 'o', color=color)  # Sample mean

    # Adjust x-axis labels
    ax.set_xticks(range(0, num_samples, x_axis_frequency))
    ax.set_xticklabels(range(1, num_samples + 1, x_axis_frequency))
    ax.legend()
    plt.grid(True)
    st.pyplot(fig)

    # Display the interval data
    st.subheader("Confidence Intervals Details")
    interval_data = {
        "Sample Index": list(range(1, num_samples + 1)),
        "Sample Mean": sample_means,
        "Lower Bound": lower_bounds,
        "Upper Bound": upper_bounds,
        "Interval Width": interval_widths,
        "Includes Population Mean": includes_population_mean
    }
    st.dataframe(interval_data)

# Streamlit UI
st.title("📊 Confidence Intervals Visualization")
st.write("""
A **Confidence Interval (CI)** provides a range of values that likely contains the true population parameter (e.g., the mean) 
based on a sample from the population. The width of the confidence interval depends on the sample size and the confidence level.

**Confidence Interval Formula:**
\[ \text{CI} = \text{Point Estimate} \pm \text{Margin of Error} \]

**Margin of Error** is calculated using:
\[ \text{Margin of Error} = \text{Critical Value} \times \text{Standard Error} \]
""")

st.subheader("Understanding Confidence Intervals")
st.write("""
- **Point Estimate**: The sample mean or proportion that estimates the population parameter.
- **Confidence Level**: The probability that the confidence interval contains the true population parameter. For example, a 95% confidence level means that if you were to take many samples and compute a CI for each, about 95% of those intervals would contain the true parameter.
- **Margin of Error**: Reflects the uncertainty around the point estimate. A higher confidence level results in a wider interval, indicating more uncertainty.
""")

st.header("Simulation: Confidence Intervals for Sample Means")

# Input widgets for various parameters
sample_size = st.slider("Sample Size (n)", min_value=1, max_value=500, value=30)
population_mean = st.number_input("Population Mean", value=0.0)
population_std = st.number_input("Population Standard Deviation", value=1.0, min_value=0.1)
num_samples = st.slider("Number of Simulations", min_value=1, max_value=1000, value=100)
confidence_level = st.slider("Confidence Level", min_value=0.80, max_value=0.99, value=0.95, step=0.01)
x_axis_frequency = st.slider("X-axis Label Frequency", min_value=1, max_value=num_samples, value=10)

# Generate and plot the graphs
plot_candlestick_intervals(num_samples, sample_size, population_mean, population_std, confidence_level, x_axis_frequency)

st.write("""
### Key Insights:
- **Sample Means Distribution**: Observing the distribution of sample means helps understand how well sample means estimate the population mean.
- **Confidence Intervals**: Visualizing confidence intervals for many samples helps assess how often the true population mean is covered by the interval.
- **Increasing Sample Size**: Larger sample sizes tend to produce narrower confidence intervals, providing a more precise estimate of the population parameter.

### Machine Learning Applications:
- **Model Evaluation**: Confidence intervals are used to evaluate the reliability of performance metrics (e.g., accuracy, precision) in machine learning models.
- **Hyperparameter Tuning**: Helps in assessing the variability of model performance across different hyperparameter settings.

### Real-World Applications:
- **Healthcare**: Estimating the effectiveness of treatments with a given confidence level.
- **Marketing**: Understanding customer preferences and predicting market trends.
""")

st.info("Feel free to adjust the parameters and observe how the confidence intervals and sample means change with different settings.")
