import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Create tabs for different sections
tabs = st.tabs(["Introduction & Assumptions", "Chi-Square Test of Independence", "Chi-Square Goodness of Fit", "Interactive Chi-Square Test"])

with tabs[0]:
    # Introduction
    st.header("What is a Chi-Square Test?")
    st.write(
        """
        A Chi-Square test is a statistical test used to determine if there is a significant association between categorical variables.
        It compares the observed frequencies in each category to the frequencies expected if there were no association between variables.
        """
    )

    # Types of Chi-Square Tests
    st.header("Types of Chi-Square Tests")
    st.write(
        """
        1. **Chi-Square Test of Independence:** 
        Determines if there is a significant association between two categorical variables.
        
        2. **Chi-Square Goodness of Fit Test:** 
        Tests if a sample data matches the expected distribution of a categorical variable.
        """
    )

    # Assumptions
    st.header("Assumptions")
    st.write(
        """
        The Chi-Square test assumes:
        - The observations are independent.
        - The data is categorical.
        - The expected frequency in each category is at least 5.
        """
    )

with tabs[1]:
    # Chi-Square Test of Independence
    st.header("Chi-Square Test of Independence")

    st.write(
        """
        The Chi-Square Test of Independence is used to determine if there is a significant relationship between two categorical variables.

        **Null Hypothesis (H0):** The two variables are independent.
        
        **Alternative Hypothesis (H1):** The two variables are not independent.

        **Test Statistic Calculation:**
        $$
        \chi^2 = \\sum \\frac{(O_i - E_i)^2}{E_i}
        $$
        Where:
        - $O_i$ = Observed frequency
        - $E_i$ = Expected frequency
        
        **Degrees of Freedom (df):** $( (r - 1) \\times (c - 1))$
        Where $r$ is the number of rows and $c$ is the number of columns in the contingency table.
        
        **Critical Value:** Based on the significance level (e.g., 0.05) and degrees of freedom.
        """
    )

    # Code for Chi-Square Test of Independence
    code_independence = '''
    import numpy as np
    from scipy import stats

    # Sample data (contingency table)
    observed = np.array([[30, 10], [20, 40]])

    # Perform Chi-Square test
    chi2_statistic, p_value, _, _ = stats.chi2_contingency(observed)

    # Display results
    print(f"Chi-Square Statistic: {chi2_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code for Chi-Square Test of Independence
    st.subheader("Code")
    st.code(code_independence, language='python')

    # Calculate and display results for Chi-Square Test of Independence
    observed = np.array([[30, 10], [20, 40]])
    chi2_statistic, p_value, _, _ = stats.chi2_contingency(observed)

    # Display results
    st.subheader("Results")
    st.write(f"Chi-Square Statistic: {chi2_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        st.success("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.info("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[2]:
    # Chi-Square Goodness of Fit Test
    st.header("Chi-Square Goodness of Fit Test")

    st.write(
        """
        The Chi-Square Goodness of Fit Test determines if a sample data matches the expected distribution.

        **Null Hypothesis (H0):** The sample data follows the expected distribution.
        
        **Alternative Hypothesis (H1):** The sample data does not follow the expected distribution.

        **Test Statistic Calculation:**
        $$
        \chi^2 = \\sum \\frac{(O_i - E_i)^2}{E_i}
        $$
        Where:
        - $O_i$ = Observed frequency
        - $E_i$ = Expected frequency
        
        **Degrees of Freedom (df):** \\( k - 1 \\)
        Where $k$ is the number of categories.
        
        **Critical Value:** Based on the significance level (e.g., 0.05) and degrees of freedom.
        """
    )

    # Code for Chi-Square Goodness of Fit Test
    code_goodness = '''
    import numpy as np
    from scipy import stats

    # Sample data (observed frequencies)
    observed = np.array([50, 35, 35])

    # Expected frequencies (assuming equal distribution)
    expected = np.array([40, 40, 40])

    # Perform Chi-Square goodness of fit test
    chi2_statistic, p_value = stats.chisquare(observed, f_exp=expected)

    # Display results
    print(f"Chi-Square Statistic: {chi2_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        print("The result is statistically significant. Reject the null hypothesis.")
    else:
        print("The result is not statistically significant. Fail to reject the null hypothesis.")
    '''

    # Display code for Chi-Square Goodness of Fit Test
    st.subheader("Code")
    st.code(code_goodness, language='python')

    # Calculate and display results for Chi-Square Goodness of Fit Test
    observed = np.array([50, 35, 35])
    expected = np.array([40, 40, 40])
    chi2_statistic, p_value = stats.chisquare(observed, f_exp=expected)

    # Display results
    st.subheader("Results")
    st.write(f"Chi-Square Statistic: {chi2_statistic:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    # Interpret results
    alpha = 0.05
    if p_value < alpha:
        st.success("The result is statistically significant. Reject the null hypothesis.")
    else:
        st.info("The result is not statistically significant. Fail to reject the null hypothesis.")

with tabs[3]:
    # Interactive Chi-Square Test
    st.title("Interactive Chi-Square Test")

    # User selects type of Chi-Square test
    test_type = st.selectbox("Choose the type of Chi-Square test:", ["Chi-Square Test of Independence", "Chi-Square Goodness of Fit"])
    alpha = st.slider("Select Significance Level (α):", 0.01, 0.10, 0.05)

    if test_type == "Chi-Square Test of Independence":
        # User input for the Chi-Square Test of Independence
        st.header("Enter your observed frequencies:")
        rows = st.number_input("Number of rows:", min_value=2, max_value=10, value=2)
        cols = st.number_input("Number of columns:", min_value=2, max_value=10, value=2)

        # Input observed data
        data = []
        for i in range(rows):
            row = st.text_input(f"Enter observed frequencies for row {i + 1} (comma-separated):", "")
            if row:
                try:
                    row_data = list(map(float, row.split(',')))
                    if len(row_data) == cols:
                        data.append(row_data)
                    else:
                        st.error(f"Row {i + 1} does not have {cols} values.")
                except ValueError:
                    st.error(f"Invalid input in row {i + 1}. Ensure all entries are numbers.")
                    
        if len(data) == rows and all(len(row) == cols for row in data):
            observed = np.array(data)
            
            # Calculate expected values using row and column totals
            row_totals = np.sum(observed, axis=1, keepdims=True)
            col_totals = np.sum(observed, axis=0, keepdims=True)
            grand_total = np.sum(observed)
            
            expected = (row_totals @ col_totals) / grand_total
            
            # Display observed and expected tables
            st.subheader("Contingency Table (Observed Frequencies)")
            st.write(observed)
            
            st.subheader("Expected Frequencies")
            st.write(expected)
            
            # Perform Chi-Square test
            chi2_statistic, p_value, _, _ = stats.chi2_contingency(observed)
            critical_value = stats.chi2.ppf(1 - alpha, (rows - 1) * (cols - 1))

            # Display results
            st.subheader("Results")
            st.write(f"Chi-Square Statistic: {chi2_statistic:.4f}")
            st.write(f"P-Value: {p_value:.4f}")
            st.write(f"Critical Value (α={alpha}): {critical_value:.4f}")
            
            # Interpret results
            if p_value < alpha:
                st.success("The result is statistically significant. Reject the null hypothesis.")
            else:
                st.info("The result is not statistically significant. Fail to reject the null hypothesis.")

            # Option to visualize observed vs expected
            if st.checkbox("Visualize Observed vs Expected Frequencies"):
                fig, ax = plt.subplots()
                indices = np.arange(rows * cols)
                observed_flat = observed.flatten()
                expected_flat = expected.flatten()
                
                ax.bar(indices - 0.2, observed_flat, 0.4, label="Observed")
                ax.bar(indices + 0.2, expected_flat, 0.4, label="Expected")
                
                ax.set_xlabel("Cells")
                ax.set_ylabel("Frequencies")
                ax.set_title("Observed vs Expected Frequencies")
                ax.legend()
                
                st.pyplot(fig)

    elif test_type == "Chi-Square Goodness of Fit":
        # User input for the Chi-Square Goodness of Fit Test
        st.header("Enter your observed and expected frequencies:")
        categories = st.number_input("Number of categories:", min_value=2, max_value=10, value=3)

        observed = st.text_input("Enter observed frequencies (comma-separated):", "")
        expected = st.text_input("Enter expected frequencies (comma-separated):", "")
        
        if observed and expected:
            try:
                observed_data = np.array(list(map(float, observed.split(','))))
                expected_data = np.array(list(map(float, expected.split(','))))
                
                if len(observed_data) != categories or len(expected_data) != categories:
                    st.error(f"Both observed and expected frequencies must have {categories} values.")
                else:
                    # Perform Chi-Square Goodness of Fit test
                    chi2_statistic, p_value = stats.chisquare(observed_data, f_exp=expected_data)
                    critical_value = stats.chi2.ppf(1 - alpha, categories - 1)

                    # Display results
                    st.subheader("Results")
                    st.write(f"Chi-Square Statistic: {chi2_statistic:.4f}")
                    st.write(f"P-Value: {p_value:.4f}")
                    st.write(f"Critical Value (α={alpha}): {critical_value:.4f}")
                    
                    # Interpret results
                    if p_value < alpha:
                        st.success("The result is statistically significant. Reject the null hypothesis.")
                    else:
                        st.info("The result is not statistically significant. Fail to reject the null hypothesis.")

                    # Option to visualize observed vs expected
                    if st.checkbox("Visualize Observed vs Expected Frequencies"):
                        fig, ax = plt.subplots()
                        indices = np.arange(categories)
                        
                        ax.bar(indices - 0.2, observed_data, 0.4, label="Observed")
                        ax.bar(indices + 0.2, expected_data, 0.4, label="Expected")
                        
                        ax.set_xlabel("Categories")
                        ax.set_ylabel("Frequencies")
                        ax.set_title("Observed vs Expected Frequencies")
                        ax.legend()
                        
                        st.pyplot(fig)

            except ValueError:
                st.error("Invalid input. Ensure all entries are numbers.")
