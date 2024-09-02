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

st.write("""
Confidence intervals (CIs) are crucial in statistical inference. They provide a range of values that likely contain the true population parameter. This app allows you to explore how different factors affect the width and placement of a confidence interval.
""")

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

        # Plot margin of error line
        ax.plot([1, 1], [lower_limit, upper_limit], color='red', linestyle='--', linewidth=2, label='Margin of Error')

        # Plot sample mean
        ax.plot(1, sample_mean, 'o', color='black', label='Sample Mean', markersize=10)

        # Plot bars for lower and upper limits
        ax.bar(0.8, lower_limit, width=0.4, color='lightblue', label='Lower Limit')
        ax.bar(1.2, upper_limit, width=0.4, color='lightgreen', label='Upper Limit')

        # Adding labels and title
        ax.set_title("Confidence Interval")
        ax.set_xlabel("Sample")
        ax.set_ylabel("Value")
        ax.set_xticks([0.8, 1.2])
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

        # Show grid lines for better readability
        # ax.grid(False, linestyle='--', alpha=0.7)

        st.pyplot(fig)

        st.write("""
        **Key Points:**
        - The **Margin of Error** represents the range within which the true population parameter is likely to lie.
        - The **Confidence Interval** is influenced by the sample size, population standard deviation, and confidence level.
        - A higher confidence level results in a wider interval, reflecting greater uncertainty about the sample mean.
        - A larger sample size or lower population standard deviation narrows the interval, providing a more precise estimate.

        **Interactive Visualization:**
        Adjust the sliders to see how changes in sample size, population standard deviation, and confidence level affect the width and placement of the confidence interval.
        """)
