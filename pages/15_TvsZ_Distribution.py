import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t, norm

# Page title and introduction
st.title('Comparison of T-distribution and Z-distribution 📈')

st.header('What are T-distribution and Z-distribution?')
st.write("""
The **T-distribution** (Student's T-distribution) and the **Z-distribution** (Standard Normal distribution) are both continuous probability distributions, but they are used in different situations. 

- **Z-distribution (Standard Normal Distribution)** assumes that the population standard deviation is known and follows a normal distribution. 
- **T-distribution** is used when the population standard deviation is unknown and the sample size is small. The shape of the T-distribution depends on the **degrees of freedom (df)**, and it gets closer to the Z-distribution as the degrees of freedom increase.

Let's compare them by adjusting the degrees of freedom using the slider below.
""")

# Slider to select degrees of freedom for T-distribution
st.sidebar.header('Control Panel')
degrees_of_freedom = st.sidebar.slider(
    "Select Degrees of Freedom (df) for T-distribution:",
    min_value=1, max_value=100, value=10, step=1
)

# Function to plot T-distribution and Z-distribution
def plot_distributions(df):
    """
    Plot the T-distribution for a given degrees of freedom (df) and Z-distribution.
    """
    x = np.linspace(-4, 4, 1000)
    
    # Z-distribution (Standard Normal Distribution)
    z_pdf = norm.pdf(x, 0, 1)
    
    # T-distribution with selected degrees of freedom
    t_pdf = t.pdf(x, df)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot Z-distribution
    sns.lineplot(x=x, y=z_pdf, ax=ax, label="Z-distribution", color="blue", linewidth=2)

    # Plot T-distribution
    sns.lineplot(x=x, y=t_pdf, ax=ax, label=f"T-distribution (df={df})", color="red", linewidth=2)

    ax.set_title('Comparison of T-distribution and Z-distribution')
    ax.set_xlabel('X values')
    ax.set_ylabel('Probability Density Function (PDF)')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# Streamlit app content
st.header('Interactive Comparison')

# Plot both distributions based on the selected degrees of freedom
plot_distributions(degrees_of_freedom)

# Additional Information
st.header('Key Differences between T-distribution and Z-distribution')
st.write("""
- The **Z-distribution** is symmetrical and follows the standard normal distribution with a mean of 0 and a standard deviation of 1.
- The **T-distribution** is also symmetrical but has heavier tails than the Z-distribution, meaning it gives more probability to extreme values. This is especially true for small degrees of freedom.
- As the **degrees of freedom** increase, the T-distribution approaches the Z-distribution.

T-distribution is widely used in **hypothesis testing** and **confidence intervals** when working with small samples and unknown population standard deviations.
""")
