import streamlit as st
import numpy as np
import scipy.stats as stats

# Title and Introduction
st.title("🔍 Hypothesis Testing")

st.write("""
Hypothesis testing is a fundamental method in statistics used to determine if there is enough evidence in a sample to infer that a certain condition holds for the entire population. This app will guide you through the concepts of hypothesis testing and allow you to explore them interactively.
""")

# Null and Alternative Hypothesis
st.header("1. Null and Alternative Hypothesis")
st.write("""
- **Null hypothesis (H0):** Assumes no significant effect or relationship between variables.
- **Alternative hypothesis (H1 or Ha):** Claims there is a significant effect or relationship.
""")

# Rejection Region Approach
st.header("2. Steps in Hypothesis Testing:")
st.write("""
1. **Formulate Hypotheses:** Define the null and alternative hypotheses.
2. **Select Significance Level:** Typically 0.05 or 0.01.
3. **Check Assumptions:** Ensure data meets test assumptions (e.g., normality).
4. **Choose Test:** Select the appropriate test (Z-test, T-test, Chi-square test, ANOVA).
5. **Calculate Test Statistic:** Use sample data to compute the test statistic.
6. **Conduct the Test:** Perform the statistical test.
7. **Make a Decision:** Reject or not reject the null hypothesis based on the test statistic.
8. **Interpret Results:** Draw conclusions and interpret the results in the context of the hypothesis.
""")

# Interactive Hypothesis Testing
st.header("3. Interactive Hypothesis Testing")

# Select Test Type
test_type = st.selectbox(
    "Select Hypothesis Test Type",
    ["Z-Test", "T-Test", "Chi-Square Test"]
)

# Input Parameters
st.subheader("Input Parameters")

# Z-Test or T-Test parameters
if test_type in ["Z-Test", "T-Test"]:
    sample_mean = st.number_input("Sample Mean", value=0.0)
    population_mean = st.number_input("Population Mean", value=0.0)
    sample_std = st.number_input("Sample Standard Deviation", value=1.0)
    sample_size = st.slider("Sample Size", min_value=2, max_value=500, value=30)
    alpha = st.slider("Significance Level (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)

# Chi-Square Test parameters
if test_type == "Chi-Square Test":
    observed_values = st.text_input("Observed Values (comma-separated)", "10, 20, 30, 40")
    expected_values = st.text_input("Expected Values (comma-separated)", "25, 25, 25, 25")
    alpha = st.slider("Significance Level (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)

st.subheader("Results")
if test_type == "Z-Test" or test_type == "T-Test":
    # Calculate the test statistic
    if test_type == "Z-Test":
        z_score = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z_score)))
    else:
        t_stat, p_value = stats.ttest_1samp([sample_mean] * sample_size, population_mean)

    st.write(f"**Test Statistic:** {z_score:.4f}")
    st.write(f"**P-Value:** {p_value:.4f}")

    # Conclusion
    if p_value < alpha:
        st.success(f"Reject the null hypothesis. (p-value < {alpha})")
    else:
        st.error(f"Fail to reject the null hypothesis. (p-value >= {alpha})")

elif test_type == "Chi-Square Test":
    # Process observed and expected values
    observed_values = list(map(float, observed_values.split(',')))
    expected_values = list(map(float, expected_values.split(',')))
    
    chi2_stat, p_value = stats.chisquare(observed_values, expected_values)

    st.write(f"**Chi-Square Statistic:** {chi2_stat:.4f}")
    st.write(f"**P-Value:** {p_value:.4f}")

    # Conclusion
    if p_value < alpha:
        st.success(f"Reject the null hypothesis. (p-value < {alpha})")
    else:
        st.error(f"Fail to reject the null hypothesis. (p-value >= {alpha})")

# Type 1 and Type 2 Errors
st.header("4. Type 1 and Type 2 Errors")
st.write("""
- **Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true.
- **Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false.
""")

# One-sided vs Two-sided Test
st.header("5. One-sided vs Two-sided Test")
st.write("""
- **One-sided test:** Used when testing for an effect in a specific direction.
- **Two-sided test:** Used when testing for an effect in either direction.
""")

# Applications of Hypothesis Testing
st.header("6. Applications of Hypothesis Testing")
st.write("""
Hypothesis testing can be applied in various fields such as:
1. **Clinical Trials:** Testing the effectiveness of new treatments or drugs.
2. **Quality Control:** Assessing the quality of products or processes.
3. **Market Research:** Comparing consumer preferences or behaviors.
4. **Finance:** Evaluating the performance of investment strategies.
5. **Social Sciences:** Analyzing relationships between social variables.
""")
