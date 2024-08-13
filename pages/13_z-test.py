import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# def plot_z_test_results_p_value(z_statistic, p_value, alpha, test_type, tail_type):
#     # Plot the Z-Test results
#     fig, ax = plt.subplots(figsize=(10, 6))
    
#     x = np.linspace(-4, 4, 1000)
#     y = stats.norm.pdf(x)
    
#     ax.plot(x, y, label='Standard Normal Distribution', color='blue')
#     ax.axvline(z_statistic, color='red', linestyle='--', label='Z-Statistic')
    
#     # Highlight the alpha regions and p-value areas
#     critical_value = stats.norm.ppf(1 - alpha / 2) if tail_type == 'Two-Tailed' else stats.norm.ppf(1 - alpha)

#     if test_type == 'One-Sample Z-Test':
#         if tail_type == 'One-Tailed':
#             if z_statistic < 0:
#                 alpha_region = np.linspace(-4, z_statistic, 1000)
#                 ax.fill_between(alpha_region, stats.norm.pdf(alpha_region), color='gray', alpha=0.3, label='Alpha Region')
#             else:
#                 alpha_region = np.linspace(z_statistic, 4, 1000)
#                 ax.fill_between(alpha_region, stats.norm.pdf(alpha_region), color='gray', alpha=0.3, label='Alpha Region')
#         elif tail_type == 'Two-Tailed':
#             alpha_region_left = np.linspace(-4, -critical_value, 1000)
#             ax.fill_between(alpha_region_left, stats.norm.pdf(alpha_region_left), color='gray', alpha=0.3, label='Alpha Region')

#             alpha_region_right = np.linspace(critical_value, 4, 1000)
#             ax.fill_between(alpha_region_right, stats.norm.pdf(alpha_region_right), color='gray', alpha=0.3)
            
#     elif test_type == 'Two-Sample Z-Test':
#         if tail_type == 'Two-Tailed':
#             alpha_region_left = np.linspace(-4, -critical_value, 1000)
#             ax.fill_between(alpha_region_left, stats.norm.pdf(alpha_region_left), color='gray', alpha=0.3, label='Alpha Region')

#             alpha_region_right = np.linspace(critical_value, 4, 1000)
#             ax.fill_between(alpha_region_right, stats.norm.pdf(alpha_region_right), color='gray', alpha=0.3)
        
#         # Highlight the p-value area
#         if z_statistic < -critical_value or z_statistic > critical_value:
#             p_value_area = np.abs(x) >= np.abs(z_statistic)
#             ax.fill_between(x, y, 0, where=p_value_area, color='red', alpha=0.3, label='P-Value Area')
#         else:
#             p_value_area = np.abs(x) <= np.abs(z_statistic)
#             ax.fill_between(x, y, 0, where=p_value_area, color='red', alpha=0.3, label='P-Value Area')

#     # Highlight whether the p-value is greater or lesser than alpha
#     if p_value < alpha:
#         st.write(f"The p-value ({p_value:.4f}) is less than the significance level (alpha = {alpha:.2f}).")
#         st.write("The p-value area is within the alpha region. **Reject the null hypothesis**.")
#     else:
#         st.write(f"The p-value ({p_value:.4f}) is greater than the significance level (alpha = {alpha:.2f}).")
#         st.write("The p-value area is outside the alpha region. **Fail to reject the null hypothesis**.")
    
#     ax.set_title('Z-Test Visualization (P-Value Approach)')
#     ax.set_xlabel('Z-Score')
#     ax.set_ylabel('Probability Density')
#     ax.legend()
#     st.pyplot(fig)


# Create tabs for the Z-Test
tabs = st.tabs(["Introduction & Assumptions", "One-Sample Z-Test", "Two-Sample Z-Test", "Interactive Z-Test"])

with tabs[0]:
    # Introduction & Assumptions
    st.header("What is a Z-Test?")
    st.write(
        """
        A Z-test is a statistical test used to determine if there is a significant difference between sample and population means, or between the means of two samples. 
        It is used when the sample size is large (typically n > 30) and the population variance is known or the sample standard deviation can be used as an estimate.
        """
    )
    
    st.header("Types of Z-Tests")
    st.write(
        """
        1. **One-Sample Z-Test:** 
        Compares the mean of a single sample to a known population mean.
        
        2. **Two-Sample Z-Test:** 
        Compares the means of two independent samples.
        """
    )
    
    st.header("Assumptions")
    st.write(
        """
        The Z-test assumes:
        - The data is normally distributed.
        - The sample size is large (n > 30).
        - The population variance is known or can be approximated using the sample variance.
        - The samples are independent (for two-sample Z-tests).
        """
    )

with tabs[1]:
    # One-Sample Z-Test
    st.header("One-Sample Z-Test Example (P-Value Approach)")
    st.write(
        """
        Suppose we want to test if the average height of a sample of 50 individuals is different from the known average height of the population, which is 170 cm. Assume a known population standard deviation of 10 cm.
        
        **Null Hypothesis (H0):** The sample mean is equal to 170 cm.
        
        **Alternative Hypothesis (H1):** The sample mean is not equal to 170 cm.
        
        **Test Statistic Calculation:**
        $$
        z = \\frac{\\bar{x} - \\mu}{\\sigma / \\sqrt{n}}
        $$
        Where:
        - $\\bar{x}$ = Sample mean
        - $\\mu$ = Population mean (170 cm)
        - $\\sigma$ = Population standard deviation
        - $n$ = Sample size
        
        **P-Value Calculation:**
        The p-value is calculated using the Z-statistic and indicates the probability of observing the sample mean, or one more extreme, assuming the null hypothesis is true.
        """
    )

    # Code for one-sample Z-Test
    code_one_sample = '''
    import numpy as np
    from scipy import stats

    # Sample data
    sample_mean = 175  # Example sample mean
    population_mean = 170
    population_std_dev = 10
    sample_size = 50

    # Calculate Z-statistic
    z_statistic = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))

    # Calculate p-value for two-tailed test
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))

    # Display results
    print(f"Z-Statistic: {z_statistic:.4f}")
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
    st.code(code_one_sample, language='python')

    # Calculate and display results
    sample_mean = 175
    population_mean = 170
    population_std_dev = 10
    sample_size = 50

    z_statistic = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))

    # Display results
    st.subheader("Results")
    st.write(f"Z-Statistic: {z_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

    # Plot results
    # alpha = 0.05
    # plot_z_test_results_p_value(z_statistic, p_value, alpha, 'One-Sample Z-Test', 'Two-Tailed')

with tabs[2]:
    # Two-Sample Z-Test
    st.header("Two-Sample Z-Test Example (P-Value Approach)")
    st.write(
        """
        Suppose we want to test if there is a significant difference between the means of two independent samples. Assume known population standard deviations for both samples.

        **Null Hypothesis (H0):** The means of the two samples are equal.
        
        **Alternative Hypothesis (H1):** The means of the two samples are not equal.
        
        **Test Statistic Calculation:**
        $$
        z = \\frac{\\bar{x}_1 - \\bar{x}_2}{\\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}}
        $$
        Where:
        - $\\bar{x}_1$ = Mean of the first sample
        - $\\bar{x}_2$ = Mean of the second sample
        - $\\sigma_1$ = Population standard deviation of the first sample
        - $\\sigma_2$ = Population standard deviation of the second sample
        - $n_1$ = Sample size of the first sample
        - $n_2$ = Sample size of the second sample
        
        **P-Value Calculation:**
        The p-value is calculated using the Z-statistic and indicates the probability of observing the difference in means, or one more extreme, assuming the null hypothesis is true.
        """
    )

    # Code for two-sample Z-Test
    code_two_sample = '''
    import numpy as np
    from scipy import stats

    # Sample data
    mean1 = 175  # Mean of the first sample
    mean2 = 165  # Mean of the second sample
    std_dev1 = 10  # Population std deviation of the first sample
    std_dev2 = 12  # Population std deviation of the second sample
    size1 = 50  # Sample size of the first sample
    size2 = 60  # Sample size of the second sample

    # Calculate Z-statistic
    z_statistic = (mean1 - mean2) / np.sqrt((std_dev1**2 / size1) + (std_dev2**2 / size2))

    # Calculate p-value for two-tailed test
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))

    # Display results
    print(f"Z-Statistic: {z_statistic:.4f}")
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
    st.code(code_two_sample, language='python')

    # Calculate and display results
    mean1 = 175
    mean2 = 165
    std_dev1 = 10
    std_dev2 = 12
    size1 = 50
    size2 = 60

    z_statistic = (mean1 - mean2) / np.sqrt((std_dev1**2 / size1) + (std_dev2**2 / size2))
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))

    # Display results
    st.subheader("Results")
    st.write(f"Z-Statistic: {z_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        st.write("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.write("The result is not statistically significant. Fail to reject the null hypothesis.")

    # Plot results
    # alpha = 0.05
    # plot_z_test_results_p_value(z_statistic, p_value, alpha, 'Two-Sample Z-Test', 'Two-Tailed')

with tabs[3]:
    # Interactive Z-Test
    st.header("Interactive Z-Test")
    st.write(
        """
        Use the interactive form below to perform a Z-Test with your own data. You can choose between a one-sample or two-sample Z-Test and see the results along with the graphical representation.
        """
    )

    test_type = st.selectbox("Select Z-Test Type:", ["One-Sample Z-Test", "Two-Sample Z-Test"])
    tail_type = st.selectbox("Select Tail Type:", ["One-Tailed", "Two-Tailed"])
    
    alpha = st.slider("Significance Level (alpha):", 0.01, 0.10, 0.05)
    
    if test_type == "One-Sample Z-Test":
        sample_mean = st.number_input("Enter the sample mean:", value=0.0)
        population_mean = st.number_input("Enter the population mean:", value=0.0)
        population_std_dev = st.number_input("Enter the population standard deviation:", value=0.0)
        sample_size = st.number_input("Enter the sample size:", value=1)

        if st.button("Calculate One-Sample Z-Test"):
            z_statistic = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))
            p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic))) if tail_type == 'Two-Tailed' else (1 - stats.norm.cdf(z_statistic)) if z_statistic > 0 else stats.norm.cdf(z_statistic)

            st.write(f"Z-Statistic: {z_statistic:.4f}")
            st.write(f"P-Value: {p_value:.4f}")

            if p_value < alpha:
                st.write("The result is statistically significant. Reject the null hypothesis.")
            else:
                st.write("The result is not statistically significant. Fail to reject the null hypothesis.")
            
            #plot_z_test_results_p_value(z_statistic, p_value, alpha, 'One-Sample Z-Test', tail_type)
    
    elif test_type == "Two-Sample Z-Test":
        mean1 = st.number_input("Enter the mean of the first sample:", value=0.0)
        mean2 = st.number_input("Enter the mean of the second sample:", value=0.0)
        std_dev1 = st.number_input("Enter the population standard deviation of the first sample:", value=0.0)
        std_dev2 = st.number_input("Enter the population standard deviation of the second sample:", value=0.0)
        size1 = st.number_input("Enter the sample size of the first sample:", value=1)
        size2 = st.number_input("Enter the sample size of the second sample:", value=1)

        if st.button("Calculate Two-Sample Z-Test"):
            z_statistic = (mean1 - mean2) / np.sqrt((std_dev1**2 / size1) + (std_dev2**2 / size2))
            p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic))) if tail_type == 'Two-Tailed' else (1 - stats.norm.cdf(z_statistic)) if z_statistic > 0 else stats.norm.cdf(z_statistic)

            st.write(f"Z-Statistic: {z_statistic:.4f}")
            st.write(f"P-Value: {p_value:.4f}")

            if p_value < alpha:
                st.write("The result is statistically significant. Reject the null hypothesis.")
            else:
                st.write("The result is not statistically significant. Fail to reject the null hypothesis.")
            
            # plot_z_test_results_p_value(z_statistic, p_value, alpha, 'Two-Sample Z-Test', tail_type)
