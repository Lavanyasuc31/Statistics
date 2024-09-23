import streamlit as st
import numpy as np
from scipy import stats

# Define tabs
tabs = st.tabs(["Introduction & Assumptions", "One-Way ANOVA", "Interactive ANOVA"])

with tabs[0]:
    # Introduction
    st.header("What is ANOVA?")
    st.write(
        """
        ANOVA (Analysis of Variance) is a statistical method used to compare the means of three or more groups to see if they are significantly different from each other.
        Unlike t-tests, which compare the means of two groups, ANOVA is used when you want to test the means across multiple groups.
        """
    )

    # Types of ANOVA
    st.header("Types of ANOVA")
    st.write(
        """
        1. **One-Way ANOVA:** 
        Compares the means of three or more independent groups based on one independent variable.
        
        2. **Two-Way ANOVA:** 
        Compares the means of groups based on two independent variables and can also assess interactions between them.
        
        3. **Repeated Measures ANOVA:** 
        Compares means where the same participants are measured under different conditions.
        """
    )

    # Assumptions
    st.header("Assumptions")
    st.write(
        """
        The ANOVA test assumes:
        - The data in each group is normally distributed.
        - The groups are independent.
        - The variances among the groups are equal (homogeneity of variances).
        - The data is measured at the interval or ratio level.
        """
    )

with tabs[1]:
    # One-Way ANOVA Example
    st.header("One-Way ANOVA Example")
    st.write(
        """
        Suppose we want to test whether the mean scores from three different teaching methods are significantly different from each other.

        **Null Hypothesis (H0):** All group means are equal.
        
        **Alternative Hypothesis (H1):** At least one group mean is different.
        
        **Test Statistic Calculation:**
        $$
        F = \\frac{\\text{Between-Group Variance}}{\\text{Within-Group Variance}}
        $$
        Where the F-statistic follows the F-distribution.

        **Degrees of Freedom:**
        - Between groups: \\( k - 1 \\)
        - Within groups: \\( N - k \\)
        - Total: \\( N - 1 \\)

        **Critical Value:** Based on the F-distribution and significance level (e.g., 0.05).
        """
    )

    # Code for One-Way ANOVA
    code_anova = '''
    import numpy as np
    from scipy import stats

    # Sample data for three groups
    group1 = [23, 21, 18, 25, 30]
    group2 = [27, 29, 26, 22, 24]
    group3 = [19, 18, 23, 20, 22]

    # Perform one-way ANOVA
    f_statistic, p_value = stats.f_oneway(group1, group2, group3)

    # Display results
    print(f"F-Statistic: {f_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code for One-Way ANOVA
    st.write("### Code for One-Way ANOVA")
    st.code(code_anova, language='python')

    # Calculate and display results for One-Way ANOVA
    group1 = [23, 21, 18, 25, 30]
    group2 = [27, 29, 26, 22, 24]
    group3 = [19, 18, 23, 20, 22]

    f_statistic, p_value = stats.f_oneway(group1, group2, group3)

    # Display results
    st.write("### Results for One-Way ANOVA")
    st.write(f"F-Statistic: {f_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[2]:
    # Interactive ANOVA
    st.header("Interactive One-Way ANOVA")

    # Input for group data
    group1 = st.text_input("Group 1 Data (comma-separated)", "23, 21, 18, 25, 30")
    group2 = st.text_input("Group 2 Data (comma-separated)", "27, 29, 26, 22, 24")
    group3 = st.text_input("Group 3 Data (comma-separated)", "19, 18, 23, 20, 22")

    if st.button("Calculate One-Way ANOVA"):
        group1 = list(map(float, group1.split(',')))
        group2 = list(map(float, group2.split(',')))
        group3 = list(map(float, group3.split(',')))

        # Perform one-way ANOVA
        f_statistic, p_value = stats.f_oneway(group1, group2, group3)

        st.write(f"F-Statistic: {f_statistic:.4f}")
        st.write(f"P-Value: {p_value:.4f}")

        # Interpret results
        if p_value < 0.05:
            st.write("The result is statistically significant. Reject the null hypothesis.")
        else:
            st.write("The result is not statistically significant. Fail to reject the null hypothesis.")
