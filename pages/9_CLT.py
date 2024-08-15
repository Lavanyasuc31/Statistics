import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the random seed for reproducibility
np.random.seed(42)

# Define a function to plot the Central Limit Theorem
def plot_clt(population_type, sample_size, num_samples):
    # Generate population based on the selected distribution
    if population_type == "Normal":
        population = np.random.normal(loc=0, scale=1, size=10000)
        population_label = "μ=0, σ=1"
    elif population_type == "Uniform":
        population = np.random.uniform(low=0, high=1, size=10000)
        population_label = "low=0, high=1"
    elif population_type == "Exponential":
        population = np.random.exponential(scale=1, size=10000)
        population_label = "λ=1"
    elif population_type == "Binomial":
        population = np.random.binomial(n=10, p=0.5, size=10000)
        population_label = "n=10, p=0.5"
    elif population_type == "Poisson":
        population = np.random.poisson(lam=3, size=10000)
        population_label = "λ=3"
    elif population_type == "Bernoulli":
        population = np.random.binomial(n=1, p=0.5, size=10000)
        population_label = "p=0.5"
    elif population_type == "Pareto":
        population = np.random.pareto(a=3, size=10000)
        population_label = "a=3"
    elif population_type == "Log-Normal":
        population = np.random.lognormal(mean=0, sigma=1, size=10000)
        population_label = "μ=0, σ=1"

    # Calculate sample means
    sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(num_samples)]
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot the population distribution
    sns.histplot(population, bins=30, kde=True, color='blue', ax=axes[0])
    axes[0].set_title(f'{population_type} Distribution (Population)\n({population_label})', fontsize=16)
    axes[0].set_xlabel('Value', fontsize=14)
    axes[0].set_ylabel('Frequency', fontsize=14)
    
    # Plot the distribution of sample means
    sns.histplot(sample_means, bins=30, kde=True, color='green', ax=axes[1])
    axes[1].set_title('Distribution of Sample Means\n(Central Limit Theorem)', fontsize=16)
    axes[1].set_xlabel('Sample Mean', fontsize=14)
    axes[1].set_ylabel('Frequency', fontsize=14)
    
    plt.tight_layout()
    st.pyplot(fig)

# Streamlit UI

st.title('🎯 Central Limit Theorem Interactive Demonstration')
st.write("""
The **Central Limit Theorem (CLT)** is one of the fundamental theorems in statistics. It states that the distribution of the 
sample means (averages) of a large number of independent and identically distributed (i.i.d.) random variables 
approaches a normal distribution, regardless of the shape of the original population distribution. This property holds true 
as long as the sample size is sufficiently large, typically \(n ≥ 30\).
""")

st.subheader("Why is the CLT Important?")
st.write("""
The CLT is the cornerstone of many statistical methods. It allows us to:
- **Make inferences about population means** from sample data.
- **Construct confidence intervals** and perform hypothesis tests.
- Justify the use of the normal distribution in many scenarios, even when the data is not normally distributed.
""")

st.header("Explore the Central Limit Theorem")

# Dropdown for population type
population_type = st.selectbox(
    "Select Population Distribution",
    ["Normal", "Uniform", "Exponential", "Binomial", "Poisson", "Bernoulli", "Pareto", "Log-Normal"]
)

# Slider for sample size
sample_size = st.slider("Sample Size (n)", min_value=1, max_value=500, value=30)

# Slider for number of samples
num_samples = st.slider("Number of Samples", min_value=100, max_value=5000, value=1000, step=100)

# Generate and plot the graphs
plot_clt(population_type, sample_size, num_samples)

# Additional educational content
st.write("""
### Key Takeaways:
- **Regardless of the original population distribution**, the distribution of the sample means tends to become normal as the sample size increases.
- **Larger sample sizes** lead to sample means that are more closely clustered around the true population mean, reducing the spread (standard error).
- The CLT provides a theoretical foundation for many statistical techniques, making it possible to use normal distribution-based methods in a wide range of applications.
""")

st.info("Try changing the population distribution and see how the shape of the sample means distribution becomes more normal as the sample size increases.")

st.write("""
### Real-World Applications of CLT:
- **Quality Control**: Understanding the distribution of product dimensions, lifetimes, or error rates.
- **Finance**: Estimating the average return on investments over time.
- **Biostatistics**: Modeling the average response to a treatment in clinical trials.
- **Machine Learning**: 
    - **Model Evaluation**: Using the CLT to understand the distribution of performance metrics across different training runs or validation sets.
    - **Confidence Intervals for Predictions**: Constructing confidence intervals around predictions made by machine learning models to gauge their reliability.
    - **Assumption Testing**: Validating assumptions of normality in residuals of regression models.
""")
