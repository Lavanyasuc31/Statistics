import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the random seed for reproducibility
np.random.seed(42)

def plot_clt(population_type, sample_size, num_samples=1000):
    if population_type == "Normal":
        population = np.random.normal(loc=0, scale=1, size=10000)
    elif population_type == "Uniform":
        population = np.random.uniform(low=0, high=1, size=10000)
    elif population_type == "Exponential":
        population = np.random.exponential(scale=1, size=10000)
    elif population_type == "Binomial":
        population = np.random.binomial(n=10, p=0.5, size=10000)
    elif population_type == "Poisson":
        population = np.random.poisson(lam=3, size=10000)
    elif population_type == "Beta":
        population = np.random.beta(a=2, b=5, size=10000)
    elif population_type == "Bernoulli":
        population = np.random.binomial(n=1, p=0.5, size=10000)
    elif population_type == "Pareto":
        population = np.random.pareto(a=3, size=10000)
    elif population_type == "Log-Normal":
        population = np.random.lognormal(mean=0, sigma=1, size=10000)
    
    sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(num_samples)]
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot the population distribution
    sns.histplot(population, bins=30, kde=True, color='blue', ax=axes[0])
    axes[0].set_title(f'{population_type} Distribution (Population)')
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Frequency')
    
    # Plot the distribution of sample means
    sns.histplot(sample_means, bins=30, kde=True, color='green', ax=axes[1])
    axes[1].set_title('Distribution of Sample Means')
    axes[1].set_xlabel('Sample Mean')
    axes[1].set_ylabel('Frequency')
    
    plt.tight_layout()
    st.pyplot(fig)

# Streamlit UI

st.title('Central Limit Theorem')
st.write("""The Central Limit Theorem (CLT) states that the distribution of the sample means of a large 
number of independent and identically distributed random variables will approach a normal 
distribution, regardless of the underlying distribution of the variables.""")

st.subheader("Conditions for the CLT:")
st.write("1. The sample size is large enough, typically greater than or equal to 30.")
st.write("2. The sample is drawn from a finite population or an infinite population with a finite variance.")
st.write("3. The random variables in the sample are independent and identically distributed.")

st.header("Central Limit Theorem Demonstration")

# Dropdown for population type
population_type = st.selectbox(
    "Select Population Distribution",
    ["Normal", "Uniform", "Exponential", "Binomial", "Poisson", "Beta", "Bernoulli", "Pareto", "Log-Normal"]
)

# Slider for sample size
sample_size = st.slider("Sample Size", min_value=1, max_value=500, value=30)

# Generate and plot the graphs
plot_clt(population_type, sample_size)

st.write("""The CLT is important in statistics and machine learning because it allows us to make 
probabilistic inferences about a population based on a sample of data. For example, we can use the CLT 
to construct confidence intervals, perform hypothesis tests, and make predictions about the population 
mean based on the sample data. The CLT also provides a theoretical justification for many commonly used 
statistical techniques, such as t-tests, ANOVA, and linear regression.""")

