import numpy as np
import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt

# Function to calculate the confidence interval
def compute_confidence_interval(sample_mean, sample_size, population_std, confidence_level):
    """
    Compute the confidence interval for a given sample mean, sample size, population std, and confidence level.
    """
    if sample_size < 2:
        st.error("Sample size must be greater than 1 for confidence interval calculation.")
        return None, None, None
    
    sem = population_std / np.sqrt(sample_size)  # Standard error of the mean
    z_score = stats.norm.ppf((1 + confidence_level) / 2.)
    margin_of_error = sem * z_score
    
    lower_limit = sample_mean - margin_of_error
    upper_limit = sample_mean + margin_of_error
    
    return margin_of_error, lower_limit, upper_limit

# Streamlit UI
st.title("Factors Affecting Confidence Interval")

# Layout for input parameters and plot
col1, col2 = st.columns(2)

with col1:
    # Input widgets for various parameters
    sample_mean = st.number_input("Sample Mean", value=0.0)
    sample_size = st.slider("Sample Size", min_value=2, max_value=500, value=30)
    population_std = st.number_input("Population Standard Deviation", value=1.0, min_value=0.1)
    confidence_level = st.slider("Confidence Level", min_value=0.80, max_value=0.99, value=0.95, step=0.01)

# Calculate confidence interval
margin_of_error, lower_limit, upper_limit = compute_confidence_interval(sample_mean, sample_size, population_std, confidence_level)

with col2:
    # Display results and plot
    if margin_of_error is not None:
        st.write(f"**Margin of Error**: ±{margin_of_error:.4f}")
        st.write(f"**Lower Limit**: {lower_limit:.4f}")
        st.write(f"**Upper Limit**: {upper_limit:.4f}")

        # Plot the data
        st.subheader("Confidence Interval Visualization")

        fig, ax = plt.subplots(figsize=(12, 6))
        bar_width = 0.4
        bar_center = 1  # position of the bar on the x-axis

        # Plot bars for lower and upper limits
        ax.bar(bar_center - bar_width, lower_limit, width=bar_width, color='lightblue', label='Lower Limit', align='center')
        ax.bar(bar_center + bar_width, upper_limit, width=bar_width, color='lightgreen', label='Upper Limit', align='center')

        # Plot margin of error line
        ax.plot([bar_center - bar_width, bar_center + bar_width], [lower_limit, upper_limit], color='red', linestyle='--', linewidth=2, label='Margin of Error')

        # Plot sample mean
        ax.plot(bar_center, sample_mean, 'o', color='black', label='Sample Mean')

        # Adding labels and title
        ax.set_title("Confidence Interval")
        ax.set_xlabel("Sample")
        ax.set_ylabel("Value")
        ax.set_xticks([bar_center - bar_width, bar_center + bar_width])
        ax.set_xticklabels(["Lower Limit", "Upper Limit"])

        # Display legend
        ax.legend()

        # Slider for number of bins (used for adjusting y-axis limits)
        num_bins = st.slider("Number of Y-Axis Bins", min_value=1, max_value=20, value=5)
        
        # Adjust y-axis limits based on number of bins
        y_min = min(lower_limit, sample_mean) - abs(margin_of_error) * 0.5
        y_max = max(upper_limit, sample_mean) + abs(margin_of_error) * 0.5
        y_range = y_max - y_min
        bin_width = y_range / num_bins
        ax.set_ylim(y_min - bin_width, y_max + bin_width)

        st.pyplot(fig)
