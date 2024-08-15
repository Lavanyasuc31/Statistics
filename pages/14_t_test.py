import streamlit as st
import numpy as np
from scipy import stats

# Define tabs
tabs = st.tabs(["Introduction & Assumptions", "One-Sample t-Test", "Paired Sample t-Test", "Independent Two-Sample t-Test", "Interactive t-Test"])

with tabs[0]:
    # Introduction
    st.header("What is a t-Test?")
    st.write(
        """
        A t-test is a statistical test used to determine if there is a significant difference between the means of two groups. 
        It is commonly used when the sample sizes are small and the population variance is unknown.
        """
    )

    # Types of t-Tests
    st.header("Types of t-Tests")
    st.write(
        """
        1. **One-Sample t-Test:** 
        Compares the mean of a single sample to a known value (often the population mean).
        
        2. **Independent Two-Sample t-Test:** 
        Compares the means of two independent samples.
        
        3. **Paired Sample t-Test:** 
        Compares means from the same group at different times or under two different conditions.
        """
    )

    # Assumptions
    st.header("Assumptions")
    st.write(
        """
        The t-test assumes:
        - The data is approximately normally distributed.
        - The samples are independent (for independent t-tests).
        - The variances of the two groups are equal (for independent t-tests).
        - The data is measured at the interval or ratio level.
        """
    )

with tabs[1]:
    # One-Sample t-Test Example
    st.header("One-Sample t-Test Example")
    st.write(
        """
        Suppose we want to test if the average height of a sample of 20 individuals is different from the known average height of the population, which is 170 cm.
        
        **Null Hypothesis (H0):** The sample mean is equal to 170 cm.
        
        **Alternative Hypothesis (H1):** The sample mean is not equal to 170 cm.
        
        **Test Statistic Calculation:**
        The t-statistic is calculated as:
        $$
        t = \\frac{\\bar{x} - \\mu}{s / \\sqrt{n}}
        $$
        Where:
        - $\\bar{x}$ = Sample mean
        - $\\mu$ = Population mean (170 cm)
        - $s$ = Sample standard deviation
        - $n$ = Sample size
        
        **Degrees of Freedom (df):** \\( n - 1 \\)
        
        **Critical Value:** Based on the significance level (e.g., 0.05) and degrees of freedom.
        """
    )

    # Code Display
    code = '''
    import numpy as np
    from scipy import stats

    # Sample data
    sample_data = [175, 160, 170, 180, 165, 155, 170, 175, 160, 165] 

    # Known population mean
    population_mean = 170

    # Calculating sample mean and standard deviation
    sample_mean = np.mean(sample_data)
    sample_std_dev = np.std(sample_data, ddof=1)  # Delta degree of freedom
    sample_size = len(sample_data)

    # Calculate t_statistic and p_value
    t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)

    # Display results
    print(f"Sample Mean: {sample_mean:.2f}")
    print(f"Sample Standard Deviation: {sample_std_dev:.2f}")
    print(f"t-Statistic: {t_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code in Streamlit
    st.subheader("Code")
    st.code(code, language='python')

    # Calculate and display results
    sample_data = [175, 160, 170, 180, 165, 155, 170, 175, 160, 165]
    population_mean = 170

    sample_mean = np.mean(sample_data)
    sample_std_dev = np.std(sample_data, ddof=1)
    sample_size = len(sample_data)

    t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)

    # Display results
    st.subheader("Results")
    st.write(f"Sample Mean: {sample_mean:.2f}")
    st.write(f"Sample Standard Deviation: {sample_std_dev:.2f}")
    st.write(f"t-Statistic: {t_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[2]:
    # Paired Sample t-Test
    st.subheader("Paired Sample t-Test")

    st.write(
        """
        A paired sample t-test compares means from the same group at different times or under two different conditions.

        **Null Hypothesis (H0):** The mean difference between the paired samples is zero.
        
        **Alternative Hypothesis (H1):** The mean difference between the paired samples is not zero.

        **Test Statistic Calculation:**
        $$
        t = \\frac{\\bar{d}}{s_d / \\sqrt{n}}
        $$
        Where:
        - $\\bar{d}$ = Mean of the differences
        - $s_d$ = Standard deviation of the differences
        - $n$ = Number of pairs
        
        **Degrees of Freedom (df):** \\( n - 1 \\)
        
        **Critical Value:** Based on the significance level (e.g., 0.05) and degrees of freedom.
        """
    )

    # Code for paired t-test
    code_paired = '''
    import numpy as np
    from scipy import stats

    # Sample data (before and after treatment)
    data_before = [23, 21, 18, 25, 30, 27, 26, 22, 24, 19]
    data_after = [25, 23, 20, 27, 32, 29, 28, 24, 26, 21]

    # Calculate t_statistic and p_value
    t_statistic, p_value = stats.ttest_rel(data_before, data_after)

    # Display results
    print(f"t-Statistic: {t_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code for paired t-test
    st.write("### Code for Paired t-Test")
    st.code(code_paired, language='python')

    # Calculate and display results for paired t-test
    data_before = [23, 21, 18, 25, 30, 27, 26, 22, 24, 19]
    data_after = [25, 23, 20, 27, 32, 29, 28, 24, 26, 21]

    t_statistic_paired, p_value_paired = stats.ttest_rel(data_before, data_after)

    # Display results
    st.write("### Results for Paired t-Test")
    st.write(f"t-Statistic: {t_statistic_paired:.4f}")
    st.write(f"P-Value: {p_value_paired:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value_paired < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[3]:
    # Independent Two-Sample t-Test
    st.subheader("Independent Two-Sample t-Test")

    st.write(
        """
        An independent two-sample t-test compares the means of two independent samples.

        **Null Hypothesis (H0):** The means of the two groups are equal.
        
        **Alternative Hypothesis (H1):** The means of the two groups are not equal.

        **Test Statistic Calculation:**
        $$
        t = \\frac{\\bar{x}_1 - \\bar{x}_2}{s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}}
        $$
        Where:
        - $\\bar{x}_1$ = Mean of the first sample
        - $\\bar{x}_2$ = Mean of the second sample
        - $s_p$ = Pooled standard deviation
        - $n_1$ = Sample size of the first sample
        - $n_2$ = Sample size of the second sample
        
        **Degrees of Freedom (df):** \\( n_1 + n_2 - 2 \\)
        
        **Critical Value:** Based on the significance level (e.g., 0.05) and degrees of freedom.
        """
    )

    # Code for independent two-sample t-test
    code_indep = '''
    import numpy as np
    from scipy import stats

    # Sample data
    group1 = [24, 28, 30, 25, 27, 32, 29, 31, 26, 30]
    group2 = [22, 20, 23, 24, 21, 19, 18, 20, 22, 21]

    # Calculate t_statistic and p_value
    t_statistic, p_value = stats.ttest_ind(group1, group2, equal_var=True)

    # Display results
    print(f"t-Statistic: {t_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code for independent t-test
    st.write("### Code for Independent Two-Sample t-Test")
    st.code(code_indep, language='python')

    # Calculate and display results for independent t-test
    group1 = [24, 28, 30, 25, 27, 32, 29, 31, 26, 30]
    group2 = [22, 20, 23, 24, 21, 19, 18, 20, 22, 21]

    t_statistic_indep, p_value_indep = stats.ttest_ind(group1, group2, equal_var=True)

    # Display results
    st.write("### Results for Independent Two-Sample t-Test")
    st.write(f"t-Statistic: {t_statistic_indep:.4f}")
    st.write(f"P-Value: {p_value_indep:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value_indep < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[4]:
    # Interactive t-Test
    st.header("Interactive t-Test")

    # One-Sample t-Test
    st.subheader("One-Sample t-Test")
    sample_size = st.slider("Sample Size", min_value=2, max_value=100, value=10)
    sample_mean = st.number_input("Sample Mean", value=0.0)
    population_mean = st.number_input("Population Mean", value=0.0)
    sample_std_dev = st.number_input("Sample Standard Deviation", value=1.0)

    if st.button("Calculate One-Sample t-Test"):
        t_statistic = (sample_mean - population_mean) / (sample_std_dev / np.sqrt(sample_size))
        df = sample_size - 1
        p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df=df))

        st.write(f"t-Statistic: {t_statistic:.4f}")
        st.write(f"P-Value: {p_value:.4f}")

        if p_value < 0.05:
            st.write("The result is statistically significant. Reject the null hypothesis.")
        else:
            st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

    # Paired Sample t-Test
    st.subheader("Paired Sample t-Test")
    data_before = st.text_input("Data Before (comma-separated)", "23, 21, 18, 25, 30, 27, 26, 22, 24, 19")
    data_after = st.text_input("Data After (comma-separated)", "25, 23, 20, 27, 32, 29, 28, 24, 26, 21")

    if st.button("Calculate Paired t-Test"):
        data_before = list(map(float, data_before.split(',')))
        data_after = list(map(float, data_after.split(',')))
        t_statistic_paired, p_value_paired = stats.ttest_rel(data_before, data_after)

        st.write(f"t-Statistic: {t_statistic_paired:.4f}")
        st.write(f"P-Value: {p_value_paired:.4f}")

        if p_value_paired < 0.05:
            st.write("The result is statistically significant. Reject the null hypothesis.")
        else:
            st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

    # Independent Two-Sample t-Test
    st.subheader("Independent Two-Sample t-Test")
    group1 = st.text_input("Group 1 Data (comma-separated)", "24, 28, 30, 25, 27, 32, 29, 31, 26, 30")
    group2 = st.text_input("Group 2 Data (comma-separated)", "22, 20, 23, 24, 21, 19, 18, 20, 22, 21")

    if st.button("Calculate Independent Two-Sample t-Test"):
        group1 = list(map(float, group1.split(',')))
        group2 = list(map(float, group2.split(',')))
        t_statistic_indep, p_value_indep = stats.ttest_ind(group1, group2, equal_var=True)

        st.write(f"t-Statistic: {t_statistic_indep:.4f}")
        st.write(f"P-Value: {p_value_indep:.4f}")

        if p_value_indep < 0.05:
            st.write("The result is statistically significant. Reject the null hypothesis.")
        else:
            st.write("The result is not statistically significant. Fail to reject the null hypothesis.")
