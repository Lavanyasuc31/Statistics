import streamlit as st
import numpy as np
import scipy.stats as stats

# Title and Introduction
st.title("Hypothesis Testing")

# Null and Alternative Hypothesis
st.header("Null and Alternative Hypothesis")
st.write("""
- **Null hypothesis (H0):** Assumes no significant effect or relationship between variables.
- **Alternative hypothesis (H1 or Ha):** Claims there is a significant effect or relationship.
""")

# Rejection Region Approach
st.header("Steps involved in Hypothesis Testing:")
st.write("""

1. Formulate a Null and Alternative hypothesis.
2. Select a significance level (usually 0.05 or 0.01).
3. Check assumptions (e.g., distribution).
4. Decide which test is appropriate (Z-test, T-test, Chi-square test, ANOVA).
5. State the relevant test statistic.
6. Conduct the test.
7. Reject or not reject the Null Hypothesis.
8. Interpret the result.
""")

# Type 1 and Type 2 Errors
st.header("Type 1 and Type 2 Errors")
st.write("""
- **Type I error (False Positive):** Rejecting the null hypothesis when it is actually true.
- **Type II error (False Negative):** Failing to reject the null hypothesis when it is actually false.
""")

# One-sided vs Two-sided Test
st.header("One-sided vs Two-sided Test")
st.write("""
- **One-sided test:** Used when testing for an effect in a specific direction.
- **Two-sided test:** Used when testing for an effect in either direction.
""")

# Applications of Hypothesis Testing
st.header("5. Applications of Hypothesis Testing")
st.write("""
Hypothesis testing can be applied in various fields such as:
1. Testing the effectiveness of interventions or treatments.
2. Comparing means or proportions between groups.
3. Analyzing relationships between variables.
4. Evaluating the goodness of fit.
5. Testing the independence of categorical variables.
""")
